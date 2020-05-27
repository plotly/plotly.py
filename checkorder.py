import frontmatter as fm
from pathlib import Path, PosixPath
import sys

# path here is intended to include only posts from a single language
# _posts/r, _posts/plotly_js, _posts/python-v3, _posts/python in 'documentation'
# build/html in 'plotly.py-docs'
try:
    folder_path = str(sys.argv[1])
except:
    raise Exception("You need to specify a path!")

# check to see if enforce flag was given at command line
enforce = False
if len(sys.argv) == 3:
    if sys.argv[2] == 'enforce':
        enforce = True

categories = ["file_settings", "basic", "financial", "statistical", "scientific", "maps", "3d_charts", "multiple_axes"]

def get_post(path):
    return fm.load(str(path))

def get_front_matter(post):
    if "jupyter" in post.metadata:
        return post["jupyter"]["plotly"]
    else:
        return post.metadata

# this function will mutate the front-matter to enforce a sequential order
def enforceOrder(list_to_be_ordered):
    print(list_to_be_ordered)
    for index, post in enumerate(list_to_be_ordered):
        post_to_be_altered = fm.load(str(post))
        if folder_path == "python": # accounts for the fact that this is also run in the plotly.py-docs repo
            post_to_be_altered.metadata["jupyter"]["plotly"]['order'] = (index+2 if index>=4 else index+1)
            fm.dump(post_to_be_altered, str(post))
        else:        
            post_to_be_altered.metadata['order'] = index+1
            fm.dump(post_to_be_altered, str(post))

def is_consecutive(list_to_be_checked): 
    if folder_path in ["python", "build/html", "r", "build", "build/r"] and len(list_to_be_checked) > 0:
        list_to_be_checked = list_to_be_checked + [5]
    print(sorted(list_to_be_checked))
    return sorted(list_to_be_checked) == list(range(1, len(list_to_be_checked)+1))

def validate_front_matter(front_matter):
    if len(front_matter.keys()) > 0:
        if "display_as" in front_matter and "order" in front_matter:
            if front_matter['display_as'] in categories:
                return True
        else:
            return False
    else:
        return False

def get_paths_and_orders_by_category():
    posts_by_category = {category: dict(orders=[], paths=[]) for category in categories}
    suffixes = ["md", "html"]
    if folder_path == "r":
        suffixes = ["Rmd"]
    for suffix in suffixes:
        for path in Path(folder_path).glob("**/*."+suffix): 
            if ".ipynb_checkpoints" not in str(path):
                post = get_post(path)
                front_matter = get_front_matter(post)
                if "display_as" in front_matter:
                    post_category = front_matter['display_as'] 
                    if post_category in posts_by_category and validate_front_matter(front_matter):
                        posts_by_category[post_category]["paths"].append(path)
                        posts_by_category[post_category]["orders"].append(front_matter['order'])
    return posts_by_category

def check_order():
    posts_by_category = get_paths_and_orders_by_category()
    for category in categories:
        print(category)
        orders = posts_by_category[category]["orders"]
        paths = posts_by_category[category]["paths"]
        sorted_paths = [path for order, path in sorted(zip(orders, paths))]
        if not is_consecutive(posts_by_category[category]["orders"]):
            print("Order is not sequential! **CHECK NOT PASSED** in '{}' display_as!".format(category))
            if enforce is True:
                print("ENFORCING CORRECT ORDER! for {}\n".format(category))
                enforceOrder(sorted_paths)
            else:
                arg = folder_path 
                if folder_path == "build/html":
                    arg = "python"
                if folder_path == "build":
                    arg = "r"
                raise Exception("Order is not sequential! **CHECK NOT PASSED** in '{}' display_as! Run 'python check-or-enforce-order.py {} enforce' to resolve!".format(category, arg))
        else:
            print("*Check Passed!*\n")

print("**********************************************")
print("Order of '{}' Before Enforcing!".format(folder_path))
print("**********************************************\n")

check_order()

if enforce is True:
    print("*******************************************")
    print("Order of '{}' After Enforcing!".format(folder_path))
    print("*******************************************\n")
    check_order()
