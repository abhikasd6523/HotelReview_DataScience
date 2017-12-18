import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hotrev = pd.read_csv('Hotel_Reviews.csv')

#Filling the null reviews of the Hotels with 0

hotrev['reviews.rating']=hotrev['reviews.rating'].fillna(0)
#print(hotrev['name'][hotrev['city']=='Albert Lea'])


##########################


#For bringing the Reviews range to out of 5
for i in range(0,len(hotrev)):
    if(hotrev['reviews.rating'].loc[i] > 5):
        temp = hotrev['reviews.rating'].loc[i]
        newtemp = (temp/10)*5
        hotrev.at[i,'reviews.rating'] = newtemp


##########################


#Listing the Unique Cities and Hotels overall
ndarcity = (np.unique(hotrev['city']))
ndarhotel = (np.unique(hotrev['name']))

#Finding total number of Unique Cities and Hotels
lencity = len(ndarcity)
lenhotel = len(ndarhotel)

print('Number of distint city = ',lencity)
print('Number of distint hotel = ',lenhotel,'\n')


##########################


#City wise number of hotels
city_numof_hotels = pd.DataFrame(columns=['City','NumofHotels'])

for i in range(lencity):
    city_numof_hotels.loc[i] = (ndarcity[i],len(np.unique(hotrev['name'][hotrev['city']==ndarcity[i]])))

city_numof_hotels.to_csv('Final_City_Numof_Hotels.csv')
#print(city_numof_hotels)
print('City with Maximum hotels:')
print((city_numof_hotels['City'][city_numof_hotels['NumofHotels'] == max(city_numof_hotels['NumofHotels'])]),max(city_numof_hotels['NumofHotels']))
print('\n')


##########################


#Hotel wise Avg Review
final_hotels_list = pd.DataFrame(columns=['Hotel_Name','Avg_Review','Percentage'])

for i in range(40):
    final_hotels_list.loc[i] = (ndarhotel[i],(np.mean(hotrev['reviews.rating'][hotrev['name'] == ndarhotel[i]])),(((np.mean(hotrev['reviews.rating'][hotrev['name'] == ndarhotel[i]]))/5)*100))

final_hotels_list.to_csv('Final_Hotel_List_Review.csv')
#print(hotels_list)

print('Hotel with Maximum Average Review')
print((final_hotels_list['Hotel_Name'][final_hotels_list['Avg_Review'] == max(final_hotels_list['Avg_Review'])]),max(final_hotels_list['Avg_Review']))
#print (np.mean(hotrev['reviews.rating'][hotrev['name'] == 'Agate Beach Motel']))

l = list(range(len(final_hotels_list['Hotel_Name'])))
#plt.xticks(l,final_hotels_list['Hotel_Name'],rotation = 'vertical')
#plt.bar(l,final_hotels_list['Avg_Review'],align='center')
#plt.title("Average Review per Hotel")
#plt.show()


##########################


#City wise Avg Review
city_hotels_avg = pd.DataFrame(columns=['City','Avg_Review'])

for i in range(lencity):
    city_hotels_avg.loc[i] = (ndarcity[i],(np.mean(hotrev['reviews.rating'][hotrev['city'] == ndarcity[i]])))

city_hotels_avg.to_csv('Final_City_Avg.csv')

city_hotels_avg = city_hotels_avg.head(40)

c = list(range(len(city_hotels_avg['City'])))
plt.xticks(c,city_hotels_avg['City'],rotation = 'vertical')
plt.bar(c,city_hotels_avg['Avg_Review'],align='center')
plt.title("Average Review per City")
plt.show()