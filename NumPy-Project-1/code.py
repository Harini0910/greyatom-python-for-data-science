# --------------

# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#path = 'file.csv'
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header = 1)

#Code starts here

print("\n Data : \n\n", data)
print("\n Type of data : \n\n", type(data))

#New_record = np.array(new_record)
census = np.concatenate((new_record, data))
print("\n Census : ", census)

print(data.shape)

print(census.shape)



# age_c = census[:,0]
# age = np.asarray(age_c)
age = census[:,0]
print("\n\n Age : ",age)

max_age = age.max()
print("\n\n Maximum Age is : ",max_age)

min_age = age.min()
print("\n\n Minimum Age is : ",min_age)

age_mean = age.mean()
print("\n\n Mean of the age is : ",np.round(age_mean,2))

age_std = np.std(age)
print("\n\n Standard deviation of the Age is : ",np.round(age_std,2))





race_0=census[census[:,2]==0]
print("\n\n Race with value 0 is \n", race_0)

race_1 = census[census[:,2]==1]
print("\n\n Race with value 1 is \n",race_1)

race_2 = census[census[:,2]==2]
print("\n\n Race with value 2 is \n",race_2)

race_3 = census[census[:,2]==3]
print("\n\n Race with value 3 is \n",race_3)

race_4 = census[census[:,2]==4]
print("\n\n Race with value 4 is \n",race_4)

len_0 = len(race_0)
print("\n\n length of race 0 is \n",len_0)
len_1 = len(race_1)
print("\n\n length of race 1 is \n",len_1)
len_2 = len(race_2)
print("\n\n length of race 2 is \n",len_2)
len_3 = len(race_3)
print("\n\n length of race 3 is \n",len_3)
len_4 = len(race_4)
print("\n\n length of race 4 is \n",len_4)



tmp = [len_0, len_1, len_2, len_3, len_4] #python list
m_r  = np.array(tmp) #numpy array
minority_race = list(m_r).index(min(m_r)) # i will return index of 2, which is 1
print("\n\n Minority race is : ",minority_race)



senior_citizens = census[census[:,0] > 60]
print("\n\n Senior Citizens whose age greater than 60 are : \n",senior_citizens)

working_hours_sum=senior_citizens.sum(axis=0)[6]
print("\n\n Working hours sum : ",working_hours_sum)

senior_citizens_len = len(senior_citizens)
print("\n\n Length of senior citizens : ",senior_citizens_len)

avg_working_hours = working_hours_sum / senior_citizens_len
print("\n\n Average working hours is : ",np.round(avg_working_hours,2))



high = census[census[:,1] > 10]

low = census[census[:,1] <= 10]

avg_pay_high = high.mean(axis=0)[7]
print("\n\n Average high pay is : ",np.round(avg_pay_high,2))

avg_pay_low = low.mean(axis = 0)[7]
print("\n\n Average low pay is : ",np.round(avg_pay_low,2))

result = np.array_equal(avg_pay_high, avg_pay_low)
print("\n\n Fianl result is : ",result)







