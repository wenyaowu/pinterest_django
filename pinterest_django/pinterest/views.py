from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from models import Pin, Category, Board
from forms import PinForm


def index(request):
    context_dict = {}
    pins = Pin.objects.all()[:25]
    context_dict['pins'] = pins
    return render(request, 'pinterest/index.html', context_dict)


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
        form.base_fields['board'].help_text = 'Choose a Board(s): '

    context_dict = {'form': form}

    return render(request, 'pinterest/create_pin.html', context_dict)

@login_required
def my_boards(request, user_id):

    context_dict = {}
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        pass  # Handle user doesn't exists

    boards = Board.objects.filter(user=user)
    for board in boards:
        board.pin = Pin.objects.filter(board=board)[0]  # Get the first pin in the board for preview.
    context_dict['boards'] = boards

    return render(request, 'pinterest/my_boards.html', context_dict)
