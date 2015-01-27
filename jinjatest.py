# Import the Jinja2 templating engine
import jinja2

# data is a dict containing the data to populate into the template
data = {'friend': 'Jim'}

# Create a template from a string
tp = jinja2.Template('Hello {{friend}}')

# render the template into a string
output_str = tp.render(data)
print output_str



## Using a template file. Load template files from the current directory
env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
tp = env.get_template('todo-template.html')
output_str = tp.render(data)
print output_str

