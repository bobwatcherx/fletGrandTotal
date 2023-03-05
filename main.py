from flet import *



def main(page:Page):
	page.scroll = "auto"
	listfood = Column(scroll="always")
	result_buy = Column()
	grand_total = Text(0,weight="bold")

	# AND I CREATE FAKE NAME AND PRICE DATA
	food = [
	{"name":"burger","price":8000},
	{"name":"Cheese pasta","price":76400},
	{"name":"milk","price":90233},
	{"name":"coca cola","price":78400},
	{"name":"pepsi","price":65200},
	{"name":"burger meal","price":98500},
	{"name":"potato Cheese","price":24200},
	{"name":"soda ","price":3400},
	{"name":"bar ","price":56000},

	]

	def addtocart(e):
		# NOW ADD YOU CHOICES MENU TO CARt
		# AND CALCULATE TOTAL ALL PRICE YOU SELECT
		data = e.control.data
		grand_total.value +=data['price']

		# AND PUSH YOU CHOICES TO result_buy
		result_buy.controls.append(
			Container(
				content=Row([
					Text(data['name']),
					Text(data['price']),
					])

				)

			)
		page.update()


	def showcart(e):
		# SHOW CONTAINER CHECK CART
		page.overlay.append(check_cart)
		page.update()

	def closecart(e):
		# CLOSE CONTAINER CART 
		page.overlay.remove(check_cart)
		page.update()


	for x in food:
		listfood.controls.append(
		ListTile(
			title=Text(x['name'],size=25),
			subtitle=Row([
				Text(f"price {x['price']}",weight="bold"),
				TextButton("buy",
					data=x,
					on_click=addtocart

					)

				])
			)

			)


	# CREATE CART CONTAINER FOR SEE YOU BUY 
	check_cart = Container(
		bgcolor="yellow200",
		margin=30,
		padding=10,
		content=Column([
			Row([
			Text("you total cart and item",weight="bold"),
			IconButton("close",
				icon_color="red",
				on_click=closecart
				)

				]),
			result_buy,
			Divider(),
			Row([
			Text("grand total",size=25,weight="bold"),
			grand_total

			],alignment="spaceBetween")

			])
		)



	# CREATE FLOATING ACTION BUTTON
	page.floating_action_button = FloatingActionButton(
		icon="add",
		bgcolor="blue",
		on_click=showcart
		)


	page.add(
	Column([
		listfood
		])

		)

flet.app(target=main)
