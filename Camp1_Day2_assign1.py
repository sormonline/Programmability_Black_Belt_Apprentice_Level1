Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

attended = 0
strSessions = Sessions_Attended["sessions"].split(",")
for session in strSessions:
    if not session.strip() == "":
        attended += 1
print("I have attended", attended, "sessions!!")

# Eg. 
# Sessions_Attended = {'sessions' : '1011,2344,'}
# Answer:
# I have attended 2 sessions!!