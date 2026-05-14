#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")
data


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")
ages = data['Life.Expectancy.at.Birth..Both.Sexes']
plt.hist(ages)
plt.xlabel('Life.Expectancy.at.Birth..Both.Sexes')
plt.ylabel('Frequency')
plt.title('Life expectency for both gender')
plt.show()
plt.savefig('frequency_distribution.png')


# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("census2002_2022.csv")
ages = data['Under.Age.5.Mortality..Both.Sexes']
data
print(data.describe())

plt.hist(data['Life.Expectancy.at.Birth..Females'])
plt.title('Histogram of Variable 1')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()



# In[21]:


import pandas as pd

data = pd.read_csv('census2002_2022.csv')

year = 2022
filtered_data = data[data['Year'] == year]

variable = 'Life.Expectancy.at.Birth..Both.Sexes'
grouped_data = filtered_data[variable].value_counts()
print(grouped_data.describe())


# In[30]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")
year = 2022

year = 2022
filtered_data = data[data['Year'] == year]
sorted_data = filtered_data.sort_values('Life.Expectancy.at.Birth..Both.Sexes', ascending=True)
highest_country = sorted_data.iloc[0]['Country.Area.Name']
highest_value = sorted_data.iloc[0]['Life.Expectancy.at.Birth..Both.Sexes']
print("The country with the highest life expectancy at birth for both sexes in {} is {} with a value of {:.2f}".format(year, highest_country, highest_value))


# In[31]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")
year = 2022
filtered_data = data[data['Year'] == year]
grouped_data = filtered_data.groupby('Region')['Life.Expectancy.at.Birth..Males'].mean()
print(grouped_data)


# In[37]:


import matplotlib.pyplot as plt

year = 2022
filtered_data = data[data['Year'] == year]
grouped_data = filtered_data.groupby('Region')['Life.Expectancy.at.Birth..Females'].mean().sort_values(ascending=False)

plt.bar(grouped_data.index, grouped_data.values)
plt.xticks(rotation=90)
plt.title("Average Life Expectancy at Birth for Females by Region in {}".format(year))
plt.xlabel("Region")
plt.ylabel("Life Expectancy at Birth for Females")
plt.show()


# In[2]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")

year = 2022
filtered_data = data[data['Year'] == year]
grouped_data = filtered_data.groupby('Region')['Life.Expectancy.at.Birth..Both.Sexes'].mean()

statistics = grouped_data.describe()
print(statistics)


# In[2]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")
year = 2022
filtered_data = data[data['Year'] == year]
average_life_expectancy = filtered_data.groupby('Region')['Life.Expectancy.at.Birth..Both.Sexes'].mean()
print(average_life_expectancy)


# In[3]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")
year = 2022
filtered_data = data[data['Year'] == year]


average_life_expectancy = filtered_data['Life.Expectancy.at.Birth..Both.Sexes'].mean()

print("Average life expectancy for both genders in 2022: {:.2f}".format(average_life_expectancy))


# In[119]:


country = 'Monaco'
year = 2022
filtered_data = data[(data['Location'] == country) & (data['Year'] == year)]

life_expectancy_male = filtered_data.loc[filtered_data['Sex'] == 'Male', 'Life.Expectancy.at.Birth..Both.Sexes'].values[0]
life_expectancy_female = filtered_data.loc[filtered_data['Sex'] == 'Female', 'Life.Expectancy.at.Birth..Both.Sexes'].values[0]

print("Life expectancy for males in Monaco in 2022: {:.2f}".format(life_expectancy_male))
print("Life expectancy for females in Monaco in 2022: {:.2f}".format(life_expectancy_female))


# In[8]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")
country = 'Monaco'
year = 2022
gender = 'Female'
filtered_data = data[(data['Country.Area.Name'] == country) & (data['Year'] == year) ]

max_life_expectancy = filtered_data['Life.Expectancy.at.Birth..Females'].max()

print("Maximum life expectancy for women in Monaco in 2022: {:.2f}".format(max_life_expectancy))


# In[98]:


import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")
year = 2022
variable = 'Under.Age.5.Mortality..Females'
filtered_data = data[data['Year'] == year]

grouped_data = filtered_data.groupby('Region')[variable].mean()

plt.bar(grouped_data.index, grouped_data.values)
plt.xticks(rotation=90)
plt.title("Average Under 5 Mortality Rate for females by Region in {}".format(year))
plt.xlabel("Region")
plt.ylabel("Under 5 Mortality Rate for Males")
plt.show()


# In[89]:


import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")
year = 2022
variables = ['Under.Age.5.Mortality..Males', 'Under.Age.5.Mortality..Females', 'Under.Age.5.Mortality..Both.Sexes']
filtered_data = data[data['Year'] == year]
labels = ['male', 'female', 'both gender']

data_list = [filtered_data[var] for var in variables]

plt.boxplot(data_list, labels=labels)
plt.title("Box Plot of Under 5 Mortality Rates in 2022")
plt.ylabel("Under 5 Mortality Rate")
plt.show()


# In[28]:


import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")

year = 2022
variables = ['Under.Age.5.Mortality..Males', 'Under.Age.5.Mortality..Females', 'Under.Age.5.Mortality..Both.Sexes']
filtered_data = data[data['Year'] == year]
summary_statistics = filtered_data[variables].describe()

print(summary_statistics)


# In[118]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")
subregion_of_interest = 'East Asia & Pacific'

filtered_data = data[data['Subregion'] == subregion_of_interest]

variance_within_subregion = filtered_data['Variable'].var()
std_within_subregion = filtered_data['Variable'].std()

mean_of_interest = filtered_data['Variable'].mean()
median_of_interest = filtered_data['Variable'].median()

other_subregions = data[data['Subregion'] != subregion_of_interest]
mean_other_subregions = other_subregions.groupby('Subregion')['Variable'].mean()
median_other_subregions = other_subregions.groupby('Subregion')['Variable'].median()


# In[117]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")


subregion_of_interest = 'Asia'
filtered_data = data[data['Region'] == subregion_of_interest]

variance_within_subregion = filtered_data['Variable'].var()
std_within_subregion = filtered_data['Variable'].std()

mean_of_interest = filtered_data['Variable'].mean()
median_of_interest = filtered_data['Variable'].median()

other_subregions = data[data['Region'] != subregion_of_interest]
mean_other_subregions = other_subregions['Variable'].mean()
median_other_subregions = other_subregions['Variable'].median()


# In[116]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")

subregion_of_interest = 'Asia'

filtered_data = data[data['Region'] == subregion_of_interest]

variance_within_subregion = filtered_data['Variable'].var()
std_within_subregion = filtered_data['Variable'].std()

mean_of_interest = filtered_data['Variable'].mean()
median_of_interest = filtered_data['Variable'].median()


other_subregions = data[data['Region'] != subregion_of_interest]
mean_other_subregions = other_subregions['Variable'].mean()
median_other_subregions = other_subregions['Variable'].median()


# In[115]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")

subregion_of_interest = 'East Asia & Pacific'
filtered_data = data[(data['Subregion'] == subregion_of_interest) & (data['Year'] == 2022)]


variance_within_subregion = filtered_data['Variable'].var()
std_within_subregion = filtered_data['Variable'].std()


mean_of_interest = filtered_data['Variable'].mean()
median_of_interest = filtered_data['Variable'].median()

other_subregions = data[(data['Subregion'] != subregion_of_interest) & (data['Year'] == 2022)]
mean_other_subregions = other_subregions.groupby('Subregion')['Variable'].mean()
median_other_subregions = other_subregions.groupby('Subregion')['Variable'].median()




# In[114]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")
region_of_interest = 'Asia'

filtered_data = data[(data['Region'] == region_of_interest) & (data['Year'] == 2022)]

variances = filtered_data.groupby('Subregion')['Variable'].var()
stds = filtered_data.groupby('Subregion')['Variable'].std()

means = filtered_data.groupby('Subregion')['Variable'].mean()
medians = filtered_data.groupby('Subregion')['Variable'].median()


# In[113]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")
region_of_interest = 'Asia'

filtered_data = data[(data['Region'] == region_of_interest) & (data['Year'] == 2022)]

summary = filtered_data.groupby('Subregion')['Variable'].describe()

print("Statistical Summary -", region_of_interest, "in 2022")
print(summary)


# In[38]:


import pandas as pd
df = pd.read_csv("census2002_2022.csv")

asia_df = df[df['Region'] == 'Asia']
male_life_exp_2022 = asia_df[['Subregion', 'Life.Expectancy.at.Birth..Males']][asia_df['Year'] == 2022].dropna()

male_life_exp_summary = male_life_exp_2022.groupby('Subregion')['Life.Expectancy.at.Birth..Males'].describe()

print(male_life_exp_summary)


# In[39]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")

region_of_interest = 'Asia'
filtered_data = data[(data['Region'] == region_of_interest) & (data['Year'] == 2022)]

plt.figure(figsize=(10, 6))
plt.boxplot(filtered_data['Life.Expectancy.at.Birth..Males'], showfliers=False)
plt.xlabel('Subregion')
plt.ylabel('Life Expectancy (Males)')
plt.title('mortality rate for both gender across Subregions in afroca (2022)')
plt.xticks(ticks=range(1, len(filtered_data['Subregion'].unique()) + 1), labels=filtered_data['Subregion'].unique(), rotation=45)
plt.tight_layout()
plt.show()


# In[41]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")

filtered_data = data[(data['Region'] == 'Asia') & (data['Year'] == 2022)]
grouped_data = filtered_data.groupby('Subregion')


life_expectancy_summary = grouped_data['Life.Expectancy.at.Birth..Both.Sexes'].describe()
mortality_rate_summary = grouped_data['Under.Age.5.Mortality..Both.Sexes'].describe()


print("Statistical Summary for Life Expectancy (Both Sexes) in Asia - 2022")
print(life_expectancy_summary)
print()
print("Statistical Summary for Mortality Rate Under 5 (Both Sexes) in Asia - 2022")
print(mortality_rate_summary)


plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.boxplot(grouped_data['Life.Expectancy.at.Birth..Both.Sexes'].apply(list))
plt.xlabel('Subregion')
plt.ylabel('Life Expectancy (Both Sexes)')
plt.title('Distribution of Life Expectancy across Subregions in Asia (2022)')

plt.tight_layout()
plt.show()


# In[52]:


import pandas as pd
data = pd.read_csv("census2002_2022.csv")

asia_data = data[data['Region'] == 'Africa']
subregions = asia_data['Subregion'].unique()

print("Subregions in Asia:")
for subregion in subregions:
    print(subregion)


# In[67]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")


filtered_data = data[(data['Region'] == 'Africa') & (data['Year'] == 2022)]

grouped_data = 


# In[76]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")

filtered_data = data[(data['Region'] == 'Africa') & (data['Year'] == 2022)]
grouped_data = filtered_data.groupby('Subregion')

subregions = []
life_expectancy_values = []


for subregion, sub_data in grouped_data:
    subregions.append(subregion)
    life_expectancy_values.append(sub_data['Under.Age.5.Mortality..Both.Sexes'].values)


plt.figure(figsize=(10, 6))
plt.boxplot(life_expectancy_values, labels=subregions)
plt.xlabel('Subregion')
plt.ylabel('Life Expectancy of both gender')
plt.title('Mortality rate for under age 5 across Subregions in Africa - 2022')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[77]:


import pandas as pd

filtered_data = data[data['Year'] == 2022]

variables = ['Life.Expectancy.at.Birth..Both.Sexes', 'Life.Expectancy.at.Birth..Males', 'Life.Expectancy.at.Birth..Females', 'Under.Age.5.Mortality..Both.Sexes']
subset_data = filtered_data[variables]


correlation_matrix = subset_data.corr()

print(correlation_matrix)


# In[85]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")


filtered_data = data[data['Year'] == 2022]


variables = ['Life.Expectancy.at.Birth..Both.Sexes', 'Life.Expectancy.at.Birth..Males', 'Life.Expectancy.at.Birth..Females', 'Under.Age.5.Mortality..Both.Sexes']


subset_data = filtered_data[variables]


correlation_matrix = subset_data.corr()


plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)


plt.title('Bivariate Correlation Chart - 2022')


plt.show()


# In[84]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")


filtered_data = data[data['Year'] == 2022]
x = filtered_data['Life.Expectancy.at.Birth..Both.Sexes']
y = filtered_data['Under.Age.5.Mortality..Both.Sexes']

plt.scatter(x, y)


plt.xlabel('Life Expectancy (Both Sexes)')
plt.ylabel('Under 5 Mortality Rate (Both Sexes)')
plt.title('Scatter Plot - Life Expectancy vs Under 5 Mortality Rate (2022)')


plt.show()



# In[86]:


import pandas as pd


data_2002 = data[data['Year'] == 2002]
data_2022 = data[data['Year'] == 2022]


summary_2002 = data_2002.describe()
summary_2022 = data_2022.describe()


comparison = pd.concat([summary_2002, summary_2022], keys=['2002', '2022'], axis=1)


print(comparison)


# In[92]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("census2002_2022.csv")


data_2002 = data[data['Year'] == 2002]
data_2022 = data[data['Year'] == 2022]


variable1_2002 = data_2002['Under.Age.5.Mortality..Both.Sexes']
variable1_2022 = data_2022['Under.Age.5.Mortality..Both.Sexes']
variable2_2002 = data_2002['Life.Expectancy.at.Birth..Both.Sexes']
variable2_2022 = data_2022['Life.Expectancy.at.Birth..Both.Sexes']


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))


axes[0].boxplot([variable1_2002, variable1_2022])
axes[0].set_xticklabels(['2002', '2022'])
axes[0].set_ylabel('Under 5 Mortality Rate')
axes[0].set_title('Under 5 Mortality Rate (2002 vs 2022)')


axes[1].boxplot([variable2_2002, variable2_2022])
axes[1].set_xticklabels(['2002', '2022'])
axes[1].set_ylabel('Life Expectancy')
axes[1].set_title('Life Expectancy (2002 vs 2022)')

plt.tight_layout()


plt.show()






# In[93]:


import pandas as pd
import matplotlib.pyplot as plt


data_2002 = data[data['Year'] == 2002]
data_2022 = data[data['Year'] == 2022]


mortality_2002 = data_2002['Under.Age.5.Mortality..Both.Sexes']
mortality_2022 = data_2022['Under.Age.5.Mortality..Both.Sexes']


fig, ax = plt.subplots(figsize=(8, 6))


ax.boxplot([mortality_2002, mortality_2022])
ax.set_xticklabels(['2002', '2022'])
ax.set_ylabel('Mortality Rate Under 5')
ax.set_title('Mortality Rate Under 5 Comparison (2002 vs 2022)')


plt.show()


# In[120]:


import pandas as pd
import matplotlib.pyplot as plt


data_2002 = data[data['Year'] == 2002]
data_2022 = data[data['Year'] == 2022]


mortality_2002_male = data_2002[data_2002['Sex'] == 'Male']['Under.Age.5.Mortality..Both.Sexes']
mortality_2002_female = data_2002[data_2002['Sex'] == 'Female']['Under.Age.5.Mortality..Both.Sexes']

mortality_2022_male = data_2022[data_2022['Sex'] == 'Male']['Under.Age.5.Mortality..Both.Sexes']
mortality_2022_female = data_2022[data_2022['Sex'] == 'Female']['Under.Age.5.Mortality..Both.Sexes']


fig, axes = plt.subplots(1, 2, figsize=(12, 6))


axes[0].boxplot([mortality_2002_male, mortality_2022_male])
axes[0].set_xticklabels(['2002', '2022'])
axes[0].set_ylabel('Mortality Rate Under 5')
axes[0].set_title('Mortality Rate Under 5 (Male) Comparison (2002 vs 2022)')

axes[1].boxplot([mortality_2002_female, mortality_2022_female])
axes[1].set_xticklabels(['2002', '2022'])
axes[1].set_ylabel('Mortality Rate Under 5')
axes[1].set_title('Mortality Rate Under 5 (Female) Comparison (2002 vs 2022)')


plt.tight_layout()
plt.show()


# In[97]:


import pandas as pd
import seaborn as sns

data = pd.read_csv("census2002_2022.csv")

data_2002 = data[data['Year'] == 2002]
data_2022 = data[data['Year'] == 2022]

sns.boxplot(x='Year', y='Under.Age.5.Mortality..Both.Sexes', data=data_2002)

sns.boxplot(x='Year', y='Under.Age.5.Mortality..Both.Sexes', data=data_2022)

plt.show()


# In[ ]:




