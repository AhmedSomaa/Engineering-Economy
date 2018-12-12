
import numpy as np
import matplotlib.pyplot as plt


############################################################
# __readFile:: read data from a text file
############################################################
def __readFile(filePath):
	with open(filePath) as file:
		data = file.readlines()
	data = [float (x.strip()) for x in data]
	return data

############################################################
# __getPresentWorth:: return the net present worth
############################################################
def __getPresentWorth(mylist, MARR):
	return np.npv(float (MARR), mylist)

############################################################
# __getFutureWorth:: return the net future worth
############################################################
def __getFutureWorth(MARR, nper, pv):
	return np.fv(float (MARR), nper, 0, pv)

############################################################
# __getAnnualWorth:: return the net Annual worth
############################################################
def __getAnnualWorth(MARR, nper, pv):
	return np.pmt(float (MARR), nper, pv)

############################################################
# __getIRR:: return the internal rate of return
############################################################
def __getIRR(mylist):
	return np.irr(mylist)


############################################################
# __compare:: return the greatest value of two
############################################################
def __compare(val_1, val_2):
	maxi= max(val_1, val_2)
	if maxi == val_1:
		return 1
	else:
		return 0


############################################################
# main:: Engineering Economy Project
# assumption: Cash flows are the same length
# assumption: EOY
############################################################
print('============================================================')
print('                Engineering Economy: Project')
print('============================================================')

# Read MARR from user
MARR =  float (input("Please input MARR:: "))

# lists to hold each alternative's data
data_1 = []		
data_2 = []

# read data of each alternative
data_1 = __readFile("../data/data_1.txt")
data_2 = __readFile("../data/data_2.txt")

# calculate Present, Future & Annual Worth for each method
pw_1 = __getPresentWorth(data_1, MARR)
pw_2 = __getPresentWorth(data_2, MARR)
fw_1 = __getFutureWorth(MARR, 10, -1*pw_1)
fw_2 = __getFutureWorth(MARR, 10, -1*pw_2)
aw_1 = __getAnnualWorth(MARR, 10, -1*pw_1)
aw_2 = __getAnnualWorth(MARR, 10, -1*pw_2)

# plot the CFD of each alternative
y = [0,1,2,3,4,5,6,7,8,9,10]
plt.figure()
plt.hist(y, bins=10,weights =data_1, histtype='bar', color = 'r', ec='black')
plt.xticks(y)

plt.title('Alternative 1:Cash Flow')
plt.xlabel('Years')
plt.ylabel('Value')

plt.figure()
y = [0,1,2,3,4,5,6,7,8,9,10]
plt.hist(y, bins=10, weights = data_2, histtype='bar', color = 'r', ec='black')
plt.xticks(y)

plt.title('Alternative 2:Cash Flow')
plt.xlabel('Years')
plt.ylabel('Value')

plt.show()

# ranking methods
print("############### RANKING METHODS ###############")

# present worth analysis
print("\n")
print("############### PRESENT WORTH   ###############")
if __compare(pw_1, pw_2) == 1:
	print("[PW_1:: ", pw_1, "] > ", "[PW_2:: ", pw_2, "]")
	print("Alternative 1 is recommended over alternative 2")
	print("reason: ALT-1 has more present value than ALT_2")
elif __compare(pw_1, pw_2) == 0:
	print("[PW_2:: ", pw_1, "]>", "[PW_1:: ", pw_2, "]")
	print("Alternative 2 is recommended over alternative 1")
	print("reason: ALT-2 has more present value than ALT_1")

print("\n")
# future worth analysis
print("############### FUTURE WORTH    ###############")
if __compare(fw_1, fw_2) == 1:
	print("[FW_1:: ", fw_1, "]>", "[FW_2:: ", fw_2, "]")
	print("Alternative 1 is recommended over alternative 2")
	print("reason: ALT-1 has more future value than ALT_2")
elif __compare(fw_1, fw_2) == 0:
	print("[FW_2:: ", fw_2, "]>", "[FW_1:: ", fw_1, "]")
	print("Alternative 2 is recommended over alternative 1")
	print("reason: ALT-2 has more future value than ALT_1")

print("\n")
# annual worth analysis
print("############### ANNUAL WORTH    ###############")
if __compare(aw_1, aw_2) == 1:
	print("[AW_1:: ", aw_1, "]>", "[AW_2:: ", aw_2, "]")
	print("Alternative 1 is recommended over alternative 2")
	print("reason: ALT-1 has more annual value than ALT_2")
elif __compare(fw_1, fw_2) == 0:
	print("[AW_2:: ", aw_2, "]>", "AW_1:: ", aw_1, "]")
	print("Alternative 2 is recommended over alternative 1")
	print("reason: ALT-2 has more annual value than ALT_1")

print("\n")
# ranking methods
print("############### INCREMENTAL METHODS ###############")

# internal rate of return analysis
print("############### IRR    			   ###############")
if __compare(-1*data_1[0], -1*data_2[0]) == 1:
	irr_2 = __getIRR(data_2)
	if irr_2 > MARR:
		print("The alternative 2 is economically justified as IRR > MARR")
		print("starting the incremental step")
		# [x + y for x, y in zip(first, second)]
		incremental = [ d_1 - d_2 for d_1, d_2 in zip (data_1, data_2) ]
		irr_incremental = __getIRR(incremental)
		if irr_incremental > MARR:
			print("The extra payments for alternative 2 to reach alternative 1 is economically justified as IRR > MARR")
			print("ALT-1 is recommended over ALT-2")
		else:
			print("The extra payments for alternative 2 to reach alternative 1 isn't economically justified as IRR > MARR")
			print("ALT-2 is recommended over ALT-1")
	else:
		irr_1 = __getIRR(data_1)
		if irr_1 > MARR:
			print("The alternative 1 is economically justified as IRR > MARR")
			print("ALT-1 is recommended")
		else:
			print("The two alternatives aren't economically justified")
			print("The project is not recommended")
elif __compare(-1*data_1[0], -1*data_2[0]) == 0:
	irr_1 = __getIRR(data_1)
	if irr_1 > MARR:
		print("The alternative 1 is economically justified as IRR > MARR")
		print("starting the incremental step")
		incremental = [ d_1 - d_2 for d_1, d_2 in zip (data_1, data_2) ]
		irr_incremental = __getIRR(incremental)
		if irr_incremental > MARR:
			print("The extra payments for alternative 1 to reach alternative 2 is economically justified as IRR > MARR")
			print("ALT-2 is recommended over ALT-1")
		else:
			print("The extra payments for alternative 1 to reach alternative 2 isn't economically justified as IRR > MARR")
			print("ALT-1 is recommended over ALT-2")
	else:
		irr_2 = __getIRR(data_2)
		if irr_2 > MARR:
			print("The alternative 2 is economically justified as IRR > MARR")
			print("ALT-2 is recommended")
		else:
			print("The two alternatives aren't economically justified")
			print("The project is not recommended")

print("\n")
print('============================================================')
print('                Engineering Economy: EOP')
print('============================================================')