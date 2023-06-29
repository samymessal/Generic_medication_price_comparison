import importlib

# Importez le module pandas pour obtenir son chemin
pandas = importlib.import_module('pandas')
pandas_path = pandas.__file__

# Importez le module tabulate pour obtenir son chemin
tabulate = importlib.import_module('tabulate')
tabulate_path = tabulate.__file__

print("Chemin de pandas:", pandas_path)
print("Chemin de tabulate:", tabulate_path)
