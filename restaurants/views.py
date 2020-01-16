from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list" :[
    	{
    		"restaurant_name": "KFC",
    		"food_type": "Chicken"
    	}, 
    	{
    		"restaurant_name": "McDonalds",
    		"food_type": "Burgers"
    	},
    	{
    		"restaurant_name": "Caboria",
    		"food_type" : "Grilled"
    	}
    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object" : {
			"restaurant_name" : "KFC",
			"food_type" : "Chicken"
    	}

    }
    return render(request, 'detail.html', context)
