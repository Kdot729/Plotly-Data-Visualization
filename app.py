from flask import Flask, render_template, request
import backend.page as page
app = Flask(__name__,  static_url_path='', static_folder="frontend/static", template_folder="frontend/templates")

@app.route("/") 
@app.route("/home") 
def Home(): 
    return render_template(template_name_or_list="home.html")

@app.route('/graph/<string:graph>/<string:specificity>/<string:tool>')
def page_router(graph, specificity, tool):
    return page.Render_Graph(graph, specificity, tool)

@app.route('/graph/<string:Graph_Name>/<string:Tool>')
def page_router(Graph_Name, Tool):
    return page.Render_Graph(Graph_Name, Tool)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



