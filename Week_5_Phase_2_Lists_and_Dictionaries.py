
# Jason Avery
# CIS261
# Project Phase 2


def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname

#THIS IS NEW CODE BELOW
# write the code to input fromdate and todate and return the values from the function
# prompt user for the dates in the following format: mm/dd/yyyy
# no validation needed for this input, assumption is dates are entered correctly

def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input ("Enter End Date (mm/dd/yyyy): ")
    return datesworked
    
def GetHours():
    hours = float(input("Enter hours worked: "))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

# COMMENT OUT THE CODE BELOW

#def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    #print(empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")

# THIS IS NEW CODE BELOW

def printinfo(EmDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
   
    # the following NEW code below creates a for loop to read through EmpDetailsList and assign values in list to variables
    # we must also write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpList

    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
         
        # the following NEW line of code assigns TotEmployees totals to dictionary
        # we must also write code to assign TotHours, TotGrossPay, TotTax, & TotNetPay to corresponding dictionary items

        EmpTotals["TotEmp"] = TotEmployees
        HrsTotals["TotHrs"] = TotHours
        GrossPayTotals["TotGrossPay"] = TotGrossPay
        TaxTotals["TotTax"] = TotTax
        NetPayTotals["TotNetPay"] = TotNetPay
       

# COMMENT OUT THE CODE BELOW

#def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    #print()
    #print(f"Total Number Of Employees: {TotEmployees}")
    #print(f"Total Number of Hours: {TotHours:,.2f}")
    #print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    #print(f"Total Tax: {TotTax:,.2f}")
    #print(f"Total Net Pay: {TotNetPay:,.2f}")

# THIS IS NEW CODE BELOW
# use dictionary to print totals
# the following line of code prints Total Employees from the dictionary
# write code to print TotalHrs, TotGrossPay, TotTax and TotNetPay from dictionary

def PrintTotals(EmpTotals):
    print()
    print(f'Total Number of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Number of Hours: {HrsTotals["TotHrs:,.2f"]}')
    print(f'Total Gross Pay: {GrossPayTotals["TotGrossPay:,.2f"]}')
    print(f'Total Tax: {TaxTotals["TotTax:,.2f"]}')
    print(f'Total Net Pay: {NetPayTotals [TotNetPay:,.2f"]}')
 

if __name__ == "__main__":
    # COMMENT OUT THE CODE BELOW

    #TotEmployees = 0
    #TotHours = 0.00
    #TotGrossPay = 0.00
    #TotTax = 0.00
    #TotNetPay = 0.00

    # THIS IS NEW CODE BELOW
    # create emply list and dictionary

    EmpDetailList =[]
    EmpTotals ={}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break

        fromdate, todate = GetDatesWorked()

        hours = GetHours()
        
        hourlyrate = GetHourlyRate()
       
        taxrate = GetTaxRate()
        
        # COMMENT OUT THE CODE BELOW  
              
        #grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)

        # write code to insert fromdate, todate, empname, hourlyrate, and taxrate into list EmpDetail
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]

        
        #the NEW code below appends the list EmpDetail to the list EmpDetailList
        EmpDetailList.append(EmpDetail)

        # COMMENT OUT THE CODE BELOW

        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay


   #PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
    
    printinfo(EmpDetailList)
    PrintTotals(EmpTotals)


