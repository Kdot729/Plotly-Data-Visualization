from flask import Flask, request
import backend.sort.generic_sort as generic_sort
import backend.page.page_render as page_render


app = Flask(__name__,  static_url_path='', static_folder="frontend/static", template_folder="frontend/templates")


@app.route('/<string:Graph>/<string:Specificity>/<string:Tool>')
def route_page(Graph, Specificity, Tool):
    return page_render.initial_page_render(Graph, Specificity, Tool)



@app.route('/update_page', methods=['GET'])
def update_page():  

    #* Convert request.args. An ImmutableMultiDict to a regular dictionary
    frontend_dictionary = dict(request.args)

    return page_render.page_rerender(frontend_dictionary)



