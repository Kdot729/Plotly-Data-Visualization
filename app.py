from flask import Flask, request
import backend.bar.page as bar_page
import backend.scatter.page as scatter_page
import backend.page as page
app = Flask(__name__,  static_url_path='', static_folder="frontend/static", template_folder="frontend/templates")


@app.route('/scatter/basic/<string:tool>')
def route_scatter_page(tool):

    return scatter_page.initial_page_render(tool)

@app.route('/bar/count_transactions/<string:tool>')
def route_bar_page(tool):
    return bar_page.initial_page_render(tool)


@app.route('/update_page_router', methods=['GET'])
def update_page_router(): 

    #Note Convert request.args. An ImmutableMultiDict to a regular dictionary
    frontend_dictionary = dict(request.args)
    
    if frontend_dictionary["Specificity"] == "basic":
        return page.page_rerender(frontend_dictionary)
    elif frontend_dictionary["Specificity"] == "count_transactions":
        return page.page_rerender(frontend_dictionary)




