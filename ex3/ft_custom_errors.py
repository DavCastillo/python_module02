#!/usr/bin/env python3

class GardenError(Exception):
	def __init__(self, message = "Unknown garden error"):
		self.message = message

	def __str__(self):
		return (self.message)


class PlantError(GardenError):
	def __init__(self, message = "Unknown plant error"):
		self.message = message
	
	def __str__(self):
		return (self.message)


class WaterError(GardenError):
	def __init__(self, message = "Unknown water error"):
		self.message = message
		
	def __str__(self):
		return (self.message)


def raise_plant_error() -> None:
	raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
	raise WaterError("Not enough water in the tank!")


def garden_errors_tester() -> None:
	print("=== Custom Garden Errors Demo ===")

	try:
		print("\nTesting PlantError...")
		raise_plant_error()
	except PlantError as error:
		print("Caught PlantError:", error)

	try:
		print("\nTestint WaterError...")
		raise_water_error()
	except WaterError as error:
		print("Caught WaterError:", error)

	print("\nTesting catching all garden errors...")
	try:
		raise_plant_error()
	except GardenError as error:
		print("Caught GardenError:", error)

	try:
		raise_water_error()
	except GardenError as error:
		print("Caught GardenError:", error)

	print("\nAll custom errors types work correctly!")

if __name__ == "__main__":
	garden_errors_tester()

