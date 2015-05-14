from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


from models import Pin, Board
from forms import PinForm, BoardForm, PinPinForm


def index(request):
    context_dict = {}
    pins = Pin.objects.filter(repin=False)[:25]
    context_dict['pins'] = pins
    return render(request, 'pinterest/index.html', context_dict)

@login_required
def create_board(request):

    if request.method == 'POST':
        form = BoardForm(request.POST)
        user = request.user
        if form.is_valid():
            board = form.save(commit=False)
            board.user = user
            board.save()
            return redirect('/pinterest/'+str(request.user.id)+'/boards/')
        else:
            print form.errors
    else:
        form = BoardForm()
    context_dict = {'form': form}

    return render(request, 'pinterest/create_board.html', context_dict)

@login_required
def create_pin(request):

    if request.method == 'POST':
        form = PinForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/pinterest/')
        else:
            print form.errors
    else:
        form = PinForm(request.user)
        form.base_fields['board'].help_text = '  '

    context_dict = {'form': form}

    return render(request, 'pinterest/create_pin.html', context_dict)


def boards(request, user_id):

    context_dict = {}
    context_dict['user_id'] = user_id
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        pass  # Handle user doesn't exist

    boards = Board.objects.filter(user=user).order_by('-pk', 'title').distinct('pk', 'title')[:25]
    if boards:
        for board in boards:
            try:
                board.pin = Pin.objects.filter(board=board)[0]  # Get the first pin in the board for preview.
            except:
                pass
        context_dict['boards'] = boards

    return render(request, 'pinterest/boards.html', context_dict)


def board(request, user_id, board_slug):

    context_dict = {}
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        pass  # Handle user doesn't exist
    try:
        board = Board.objects.get(user=user, slug=board_slug)
        context_dict['board'] = board
    except Board.DoesNotExist:
        pass  # Handle board doesn't exist
    try:
        pins = Pin.objects.filter(board=board).order_by('-id', 'title').distinct('id', 'title')[:25]
        context_dict['pins'] = pins
    except Pin.DoesNotExist:
        pass  # No pin in current board

    return render(request, 'pinterest/board.html', context_dict)

@login_required
def like_pin(request):
    pin_id = None
    if request.method == 'GET':
        pin_id = request.GET['pin_id']
    likes = 0
    if pin_id:
        pin = Pin.objects.get(id=int(pin_id))
        if pin:
            likes = pin.likes+1
            pin.likes = likes
            pin.save()

    return HttpResponse(likes)


@login_required
def pin_pin(request, pin_id):
    try:
        pin_target = Pin.objects.get(id=pin_id)
    except Pin.DoesNotExist:
        pass  # Handle

    if request.method == 'POST':
        form = PinPinForm(request.user, pin_id, request.POST)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.title = pin_target.title
            pin.description = pin_target.description
            pin.image = pin_target.image
            pin.category = pin_target.category
            pin.likes = pin_target.likes
            pin.repin = True
            pin.save()
            form.save_m2m()  # In order to save the manytomany models.
            return redirect('/pinterest/')  # Return success to Ajax
        else:
            print form.errors  # Return fail
    else:
        form = PinPinForm(request.user, pin_id)
    context_dict = {'form': form, 'pin_id': pin_id}

    return render(request, 'pinterest/pin_pin.html', context_dict)
