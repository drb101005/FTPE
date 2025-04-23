#Task List

#List
tasks_list=["clean house","homework","walk"]
tasks_list.append("pay bills")
print("after addind tasks:",tasks_list)
tasks_list.remove("homework")
print("after removing tasks:",tasks_list)
tasks_list[1]="run"
print("after updating tasks:",tasks_list)
tasks_list.sort()
print("after sorting tasks:",tasks_list)

#Tuple
tasks_tuple=("clean house","homework","walk")
tasks_tuple=tasks_tuple+("pay bills",)
print("\nAfter addng a task to tuple:",tasks_tuple)
temp_list=list(tasks_tuple)
temp_list.remove("homework")
tasks_tuple=tuple(temp_list)
print("after removing task from tuple:",tasks_tuple)
temp_list=list(tasks_tuple)
temp_list[1]=("run")
tasks_tuple=tuple(temp_list)
print("after updating task from tuple:",tasks_tuple)
temp_list=list(tasks_tuple)
temp_list.sort()
tasks_tuple=tuple(temp_list)
print("after sorting task from tuple:",tasks_tuple)