from time import sleep
target_time = 10
word_list = ["a","b","c","D","E","F","H","I"]
select_word=0
def up_timer(secs):
    for i in range(0,secs):
        print("のこり{}秒です".format(target_time-i))
        sleep(1)
    print("時間です！")
print("選択できる言葉"+str(word_list))
for index ,word in enumerate(word_list):
    print(index,word)

select_word = int(input())
print("選択した言葉:"+str(word_list[select_word]))
up_timer(target_time)


   