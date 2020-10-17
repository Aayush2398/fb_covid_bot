import requests
import random


class GetCovidData:

	data = {}
	post_statement = "INDIA's COVID-19 UPDATE: \nState name: {}" \
					 "\nTotal Confirmed Cases: {}(+{})\nTotal Deaths: {}(+{})\nPatients Recovered:{}(+{})" \
					 "\nHope you are safe."
	updated_statement = ""

	def __init__(self):
		self.data.update({"data": "init"})

	def get_data(self):
		r = requests.get("https://api.covid19india.org/data.json")
		states_data = r.json()["statewise"]
		# print(states_data)
		# print(len(states_data))
		random_num = random.randint(0, len(states_data)-1)
		# print(random_num)
		# print(states_data[random_num])
		selected_state = states_data[random_num]
		self.updated_statement = self.post_statement.format(
			selected_state["state"], selected_state['confirmed'], selected_state['deltaconfirmed'],
			selected_state["deaths"], selected_state['deltadeaths'], selected_state['recovered'], selected_state['deltarecovered'])
		self.data = {"data": "abc"}

	def show_data(self):
		print(self.updated_statement)


if __name__ == "__main__":

	covid = GetCovidData()
	covid.show_data()
	covid.get_data()
	covid.show_data()
