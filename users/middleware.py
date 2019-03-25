def my_middleware(get_response):
    print('init被调用')

    def middleware(request):
        print('before request 被调用')
        response = get_response(request)
        print('after response 被调用')
        return response

    return middleware


def my_middleware2(get_response):
    print('init2被调用')

    def middleware(request):
        print('before request 被调用2')
        response = get_response(request)
        print('after response 被调用2')
        return response

    return middleware
