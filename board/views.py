from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import Board
from account.models import Member
from .forms import BoardForm
import logging

logger = logging.getLogger('board')
logger.setLevel(logging.DEBUG)


def index(request):
    print(a)
    return render(request, 'board/board_list.html')
    
# Create your views here.
def board_list(request) :
    logger.debug('logger = {}'.format(logger))
    logger.debug('__name__ = {}'.format(__name__))
    all_boards  = Board.objects.all().order_by('-id')
    # 변수명을 all_boards 로 바꿔주었다.
    page        = int(request.GET.get('p', 1))
    # p라는 값으로 받을거고, 없으면 첫번째 페이지로
    pagenator   = Paginator(all_boards, 10)
    # Paginator 함수를 적용하는데, 첫번째 인자는 위에 변수인 전체 오브젝트, 2번째 인자는
    # 한 페이지당 오브젝트 10개씩 나오게 설정
    boards      = pagenator.get_page(page)
    # 처음 10개가 세팅 된다.
    return render(request, 'board/board_list.html', {"boards" : boards})

def board_write(request):
    logger.debug('logger = {}'.format(logger))
    logger.debug('__name__ = {}'.format(__name__))
    if not request.session.get('user'):
        return redirect('/account/login/')
    # 세션에 'user' 키를 불러올 수 없으면, 로그인하지 않은 사용자이므로 로그인 페이지로 리다이렉트 한다.

    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            # form의 모든 validators 호출 유효성 검증 수행
            user_id = request.session.get('user')
            member = Member.objects.get(pk=user_id)
            
            board = Board()
            board.title     = form.cleaned_data['title']
            board.contents  = form.cleaned_data['contents']
            # 검증에 성공한 값들은 사전타입으로 제공 (form.cleaned_data)
            # 검증에 실패시 form.error 에 오류 정보를 저장
            
            board.writer    = member
            board.save()

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board/board_write.html', {'form': form})

def board_detail(request, pk):
    logger.debug('GET access id = {} product_detail'.format(pk))
    logger.debug('logger = {}'.format(logger))
    logger.debug('__name__ = {}'.format(__name__))
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')
        # 게시물의 내용을 찾을 수 없을 때 내는 오류 message.

    return render(request, 'board/board_detail.html', {'board':board})