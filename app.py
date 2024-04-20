from flask import Flask, request
import backend.page as page
app = Flask(__name__,  static_url_path='', static_folder="frontend/static", template_folder="frontend/templates")


@app.route('/graph/<string:graph>/<string:specificity>/<string:tool>')
def page_router(graph, specificity, tool):
    print(graph, specificity, tool)
    return page.initial_page_render(graph, specificity, tool)

@app.route('/update_page_router', methods=['GET'])
def update_page_router(): 

    #Note Convert request.args. An ImmutableMultiDict to a regular dictionary
    frontend_dictionary = dict(request.args)
    return page.page_rerender(frontend_dictionary)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



