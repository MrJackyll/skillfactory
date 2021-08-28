#slovari
catalog_item = {
	"type": "phone",
	"vendor": "Apple",
	"model": "Iphone 12",
	"price": "37.5"
	}
catalog_item ['audio_jack'] = False #add new element
catalog_item['price'] = 70 #change value of element
print (catalog_item)
print (catalog_item['price']) #вывод по ключу
item_name = catalog_item['vendor'] + " " + catalog_item['model']
print (item_name)
print (catalog_item.get('discount', 'Скидок нет')) #.get выводит значение по умолчанию если не находит элемент
print ('model' in catalog_item) #проверяем наличие элемента в словаре
print ('discount' in catalog_item)
print ('discount' not in catalog_item) #проверяем отсутсвие элемента в словаре
del catalog_item ['audio_jack']
print (catalog_item)
