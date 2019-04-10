from flask import Flask, render_template
app = Flask(__name__)

posts = [
	{
		'author': 'Jay Kiharani',
		'date_posted': 'April 10, 2019',
		'title': 'Global Payments using PayPal',
		'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet illo officia facere tempora, voluptate inventore odit veritatis voluptates unde nam quo maiores atque similique quis. Animi debitis aperiam dolorem. Assumenda, distinctio eos provident consequatur ab vel impedit nobis cupiditate fuga sapiente nulla quasi rem hic odit ratione veritatis, pariatur voluptatibus magnam non, consequuntur voluptatum? Iure repellendus exercitationem fugit, quos. Eaque rem amet magnam, neque vero ad laudantium harum natus voluptatem quam unde. Consectetur suscipit, molestias.'
	},
	{
		'author': 'Kendi Gitonga',
		'date_posted': 'April 10, 2019',
		'title': 'M2C Education in Mathare',
		'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum nostrum voluptates nihil minima repudiandae ratione, quos. Sapiente odio qui in ipsam ratione incidunt illo beatae reiciendis laborum atque numquam necessitatibus laboriosam, voluptate praesentium recusandae, adipisci voluptas. Amet obcaecati qui vitae. Quos nemo libero explicabo esse sed eveniet consequatur, sequi voluptatibus at placeat expedita, dolorem eos exercitationem animi, voluptas repellendus ullam minima illo. Ab ipsum, repellendus molestiae, minima aliquam beatae. Autem quam soluta quas obcaecati excepturi!'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
	app.run(debug=True)