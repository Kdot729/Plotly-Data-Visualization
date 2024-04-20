from flask import Flask, render_template, request
import backend.page as page
app = Flask(__name__,  static_url_path='', static_folder="frontend/static", template_folder="frontend/templates")

@app.route("/") 
@app.route("/home") 
def Home(): 
    return render_template(template_name_or_list="home.html")

@app.route('/graph/<string:graph>/<string:specificity>/<string:tool>')
def page_router(graph, specificity, tool):
    print(graph, specificity, tool)
    return page.initial_page_render(graph, specificity, tool)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



