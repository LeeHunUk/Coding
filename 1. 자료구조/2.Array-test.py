data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 연습문제1 : 위의 2차원 배열에서 9 8 7 순서로 출력
print(data[2][2])
print(data[2][1])
print(data[2][0])
print("====================")

# 연습문제2 : 다음 dataset에서 전체 이름 안에 M이 몇번 나왔는지 빈도수 출력
dataset = [
    'Braund, Mr. Owen Harris','Cumings, Mrs. John Bradley (Florence Briggs Thayer)','Heikkinen, Miss. Laina',
    'Futrelle, Mrs. Jacques Heath (Lily May Peel)','Allen, Mr. William Henry','Moran, Mr. James',
    'McCarthy, Mr. Timothy J','Palsson, Master. Gosta Leonard','Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
    'Nasser, Mrs. Nicholas (Adele Achem)','Sandstrom, Miss. Marguerite Rut','Bonnell, Miss. Elizabeth',
    'Saundercock, Mr. William Henry','Andersson, Mr. Anders Johan','Vestrom, Miss. Hulda Amanda Adolfina',
    'Hewlett, Mrs. (Mary D Kingcome) ','Rice, Master. Eugene','Williams, Mr. Charles Eugene',
    'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)','Masselmani, Mrs. Fatima','Fynney, Mr. Joseph J',
    'Beesley, Mr. Lawrence','McGowan, Miss. Anna "Annie"','Sloper, Mr. William Thompson',
    'Palsson, Miss. Torborg Danira','Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
    'Emir, Mr. Farred Chehab','Fortune, Mr. Charles Alexander','Dwyer, Miss. Ellen "Nellie"','Todoroff, Mr. Lalio']

# 나의 풀이!
check = 0
for i in dataset:
    check += i.count('M')

print(check)

# 실제 풀이!
m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index]=="M":
            m_count += 1

print(m_count)