from flask import Blueprint,render_template,request,redirect
from app import testing_system

reviews_app = Blueprint("reviews","reviews",url_prefix='/reviews')

@reviews_app.route('/',methods = ['GET','POST'])
def reviews():
    if request.method == "POST":
        author = request.form['author']
        text = request.form['text']
        testing_system.add_review(author,text)    
    
    reviews = testing_system.list_reviews()
    return render_template("reviews.html",reviews=reviews)

@reviews_app.route('/<int:review_index>/delete', methods=['POST'])
def delete_review(review_index):
    testing_system.remove_review(review_index)
    return redirect('/reviews')