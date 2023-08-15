from flask_restful import Resource


class Manager(Resource):
    def get(self):
        try:
            return dict(text='hi')
        except Exception as e:
            print(e)
            import traceback
            traceback.print_stack()