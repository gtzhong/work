'''
12-13 装饰器 六

满足复用性  不必修改指定的代码

函数是使用多个装饰器

#flask
'''


@api.route('/get',method=['GET'])
def test_javascript_http():
	p=request.args.get('name')
	return p,200

@api.route('/psw',method=['GET'])
@auth.login_required
def get_psw():
	p=request.args.get('psw')
	r=generate_password_hash(p)
	return 'aaaaaa',200