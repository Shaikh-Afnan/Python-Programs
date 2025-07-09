def cmtoinch(cm):
    return (cm/2.54)

cm = int(input("Please enter the length in cm : "))
i = cmtoinch(cm)
print(f"The length entered in inch is : {i}")

