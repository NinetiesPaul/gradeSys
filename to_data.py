import random
import pandas as pd

def group_by_rank(table):

    group_by_rank = table.groupby('Rank').agg({'Rank': 'count'})
    
    return group_by_rank

def group_by_grade(table):

    group_by_grade = table.groupby('Grade').agg({'Grade': 'count'})

    return group_by_grade

def group_by_discipline(table):

    group_by_discipline = table.groupby(['Discipline', 'Rank']).agg({'Rank': 'count'})
    
    return group_by_discipline

def to_pandas(classes, students):
#    names=[]
#
#    with open('names.txt') as f:
#        file=f.read()
#        names=file.split('\n')
#
#    names.sort()
#
#    disciplines=[]
#
#    with open('disciplines.txt') as f:
#        file=f.read()
#        disciplines=file.split('\n')
#
#    disciplines.sort()
#
    graders=[]

    for cls in classes:
        for student in students:
            graders.append([cls, student, float('{0:.1f}'.format(random.uniform(0,100)))])

    tb_graders=pd.DataFrame.from_records(graders,columns=['Discipline', 'Name','Score'])

    tb_graders.loc[tb_graders['Score']>=90,'Rank']='Excelent'
    tb_graders.loc[(tb_graders['Score']>=80) & (tb_graders['Score']<=89.9),'Rank']='Great'
    tb_graders.loc[(tb_graders['Score']>=70) & (tb_graders['Score']<=79.9),'Rank']='Good'
    tb_graders.loc[(tb_graders['Score']>=60) & (tb_graders['Score']<=69.9),'Rank']='Normal'
    tb_graders.loc[(tb_graders['Score']<=59.9) ,'Rank']='Bad'

    tb_graders.loc[tb_graders['Score']<=100,'Grade']='A+'
    tb_graders.loc[tb_graders['Score']<=96.9,'Grade']='A'
    tb_graders.loc[tb_graders['Score']<=92.9,'Grade']='A-'
    tb_graders.loc[tb_graders['Score']<=89.9,'Grade']='B+'
    tb_graders.loc[tb_graders['Score']<=86.9,'Grade']='B'
    tb_graders.loc[tb_graders['Score']<=82.9,'Grade']='B-'
    tb_graders.loc[tb_graders['Score']<=79.9,'Grade']='C+'
    tb_graders.loc[tb_graders['Score']<=76.9,'Grade']='C'
    tb_graders.loc[tb_graders['Score']<=72.9,'Grade']='C-'
    tb_graders.loc[tb_graders['Score']<=69.9,'Grade']='D+'
    tb_graders.loc[tb_graders['Score']<=66.9,'Grade']='D'
    tb_graders.loc[tb_graders['Score']<=62.9,'Grade']='D-'
    tb_graders.loc[tb_graders['Score']<=59.9,'Grade']='F'
    
    b=group_by_rank(tb_graders)
    c=group_by_grade(tb_graders)
    d=group_by_discipline(tb_graders)

    return tb_graders,b,c,d

#def group_by_rank(table):
#
#    lst=[]
#
#    for item in sorted(table['Rank'].unique()):
#        lst.append([item, len(table.loc[table['Rank']==item])])
#
#    tb_group_by_rank=pd.DataFrame.from_records(lst, columns=('Rank','Count'))
#
#    del lst
#
#    return tb_group_by_rank
    
#def group_by_rank(table):
#
#    group_by_rank = pd.DataFrame({
#            'Count': table.groupby('Rank')['Rank'].count()
#            })
#    
#    group_by_rank.reset_index(inplace=True)
#    
#    return group_by_rank
    

#    new=[]
#    for item in table['Discipline'].unique():
#        new.append(item)
#        for i in range(4):
#            new.append('')    
#    
#    group_by_discipline = pd.DataFrame({
#            'Discipline': new,
#            'Rank': sorted(table['Rank'].unique())*6,
#            'Count': table.groupby(['Discipline', 'Rank'])['Rank'].count()
#            })