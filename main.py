row1=[" 😘 ","  😒  "," 😝 "]
row2=[" 😤 "," 🤬 "," 🙄 "]
row3=[" 😴 "," 😭 "," 🥵 "]
map=[row1,row2,row3]
print (row1,"\n",row2,"\n",row3)
position=(input("Please enter the position to hide your treasure\n"))

horizontal=int(position[0])
vertical=int(position[1])
selected_row=map[horizontal-1]
selected_row[vertical-1]="x"

print (row1,"\n",row2,"\n",row3)
