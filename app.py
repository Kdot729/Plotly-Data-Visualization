from flask import Flask, request
import backend.bar.page as bar_page
import backend.scatter.page as scatter_page

app = Flask(__name__,  static_url_path='', static_folder="frontend/static", template_folder="frontend/templates")


@app.route('/scatter/basic/<string:tool>')
def route_scatter_page(tool):
    return scatter_page.initial_page_render(tool)

@app.route('/bar/count_transactions/<string:tool>')
def route_bar_page(tool):
    return bar_page.initial_page_render(tool)



@app.route('/update_scatter_page', methods=['GET'])
def update_scatter_page():  

    #* Convert request.args. An ImmutableMultiDict to a regular dictionary
    frontend_dictionary = dict(request.args)
    print(frontend_dictionary)
    return scatter_page.page_rerender(frontend_dictionary)

@app.route('/update_bar_page', methods=['GET'])
def update_bar_page():  

    #* Convert request.args. An ImmutableMultiDict to a regular dictionary
    frontend_dictionary = dict(request.args)

    return bar_page.page_rerender(frontend_dictionary)



