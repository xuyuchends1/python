#美国各州的统计数据
import pandas as pd
abbrevs_path = 'E:\phil\workspace\selfwork\python\Python Data Science Handbook\chapter3\state-abbrevs.csv'
areas_path = 'E:\phil\workspace\selfwork\python\Python Data Science Handbook\chapter3\state-areas.csv'
population_path = 'E:\phil\workspace\selfwork\python\Python Data Science Handbook\chapter3\state-population.csv'

abbrevs=pd.read_csv(abbrevs_path)
areas=pd.read_csv(areas_path)
population=pd.read_csv(population_path)
abbrevs


abbreviation_abbrevs= abbrevs.merge(population,how='right',left_on='abbreviation',right_on='state/region')
abbreviation_abbrevs.loc[abbreviation_abbrevs['state/region']=='PR','abbreviation' ]='PR'
abbreviation_abbrevs.loc[abbreviation_abbrevs['state/region']=='PR','state' ]='Puerto Rico'
abbreviation_abbrevs.drop('abbreviation',axis=1)
abbreviation_abbrevs=abbreviation_abbrevs[abbreviation_abbrevs['state/region']!='USA']

abbreviation_abbrevs_areas=areas.merge(abbreviation_abbrevs,how='right',left_on='state',right_on='state')
abbreviation_abbrevs_areas['midu']= abbreviation_abbrevs_areas['area (sq. mi)']/ abbreviation_abbrevs_areas['population']


#########################################################################################
#########################################################################################
#########################################################################################
abbrevs=pd.read_csv(abbrevs_path)
areas=pd.read_csv(areas_path)
pop=pd.read_csv(population_path)
merged=pd.merge(pop,abbrevs, how='left', left_on='state/region', right_on='abbreviation')
merged.loc[merged['state/region']=='PR','state']='Puerto Rico'
merged= merged[merged['state/region']!='USA']
merged=merged.drop(columns=['abbreviation'])
merged.dropna(how='any',inplace=True)
merged=pd.merge(merged,areas, how='left', left_on='state/region', right_on='state')

