from tkinter import *
from tkinter import messagebox
import datetime


def clearAll():
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)

    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)


def checkError():
    if (
        dayField.get() == ""
        or monthField.get() == ""
        or yearField.get() == ""
        or givenDayField.get() == ""
        or givenMonthField.get() == ""
        or givenYearField.get() == ""
    ):
        messagebox.showerror(
            "Input Error", "Please enter the birth date and given date"
        )

        clearAll()

        return -1


def calculateAge():
    value = checkError()
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)

    rsltHoursField.delete(0, END)
    rsltminutesField.delete(0, END)
    rsltSecondsField.delete(0, END)

    if value == -1:
        return
    else:
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())

        given_day = int(givenDayField.get())
        given_month = int(givenMonthField.get())
        given_year = int(givenYearField.get())

        month = [31, 28, 31, 30, 31, 30, 31, 30, 31]

        if birth_day > given_day:
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]

        if birth_month > given_month:
            given_year = given_year - 1
            given_month = given_month + 12

        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year
        calculated_hour = calculated_year * 12 * 30 * 24
        calculated_minute = calculated_year * 12 * 30 * 24 * 60
        calculated_second = calculated_year * 12 * 30 * 24 * 60 * 60

        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))
        rsltHoursField.insert(10, str(calculated_hour))
        rsltminutesField.insert(10, str(calculated_minute))
        rsltSecondsField.insert(10, str(calculated_second))



if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="light green")

    gui.title("calculator age")

    gui.geometry("800x300")

    dob = Label(gui, text="Date of Birth", bg="blue", fg="white")
    givenDate = Label(gui, text="Given Date", bg="yellow")
    resultdate = Label(gui, text="Result Date", bg="brown", fg="white")

    day = Label(gui, text="Day", bg="light green")
    month = Label(gui, text="Month", bg="light green")
    year = Label(gui, text="Year", bg="light green")

    givenday = Label(gui, text="GivenDay", bg="light green")
    givenmonth = Label(gui, text="GivenMonth", bg="light green")
    givenyear = Label(gui, text="GivenYear", bg="light green")

    rsltyears = Label(gui, text="Years", bg="light green")
    rsltmonths = Label(gui, text="Months", bg="light green")
    rsltDays = Label(gui, text="Days", bg="light green")

    rslthours = Label(gui, text="Hours", bg="light green")
    rsltminutes = Label(gui, text="Minutes", bg="light green")
    rsltsec = Label(gui, text="Seconds", bg="light green")

    resultantage = Button(
        gui, text="Resultant Age", fg="white", bg="brown", command=calculateAge
    )
    clearAllEntry = Button(gui, text="ClearAll", fg="black", bg="red", command=clearAll)

    dayField = Entry(gui, bg="blue", fg="white")
    monthField = Entry(gui, bg="blue", fg="white")
    yearField = Entry(gui, bg="blue", fg="white")

    givenDayField = Entry(gui, bg="yellow")
    givenMonthField = Entry(gui, bg="yellow")
    givenYearField = Entry(gui, bg="yellow")

    givenDayField.insert(20, datetime.datetime.now().day)
    givenMonthField.insert(20, datetime.datetime.now().month)
    givenYearField.insert(20, datetime.datetime.now().year)

    rsltYearField = Entry(gui, fg="white", bg="brown")
    rsltMonthField = Entry(gui, fg="white", bg="brown")
    rsltDayField = Entry(gui, fg="white", bg="brown")

    rsltHoursField = Entry(gui, fg="white", bg="brown")
    rsltminutesField = Entry(gui, fg="white", bg="brown")
    rsltSecondsField = Entry(gui, fg="white", bg="brown")

    dob.grid(row=0, column=1)

    day.grid(row=1, column=0)
    dayField.grid(row=1, column=1)

    month.grid(row=2, column=0)
    monthField.grid(row=2, column=1)

    year.grid(row=3, column=0)
    yearField.grid(row=3, column=1)

    givenDate.grid(row=0, column=4)

    givenday.grid(row=1, column=3)
    givenDayField.grid(row=1, column=4)

    givenmonth.grid(row=2, column=3)
    givenMonthField.grid(row=2, column=4)

    givenyear.grid(row=3, column=3)
    givenYearField.grid(row=3, column=4)

    resultantage.grid(row=12, column=3)

    resultdate.place(x= 300, y=70)

    rsltyears.grid(row=5, column=2)
    rsltYearField.grid(row=6, column=2)

    rsltmonths.grid(row=7, column=2)
    rsltMonthField.grid(row=8, column=2)

    rsltDays.grid(row=9, column=2)
    rsltDayField.grid(row=10, column=2)

    rslthours.grid(row=5, column=3)
    rsltHoursField.grid(row=6, column=3)

    rsltminutes.grid(row=7, column=3)
    rsltminutesField.grid(row=8, column=3)

    rsltsec.grid(row=9, column=3)
    rsltSecondsField.grid(row=10, column=3)

    clearAllEntry.grid(row=12, column=2)

    gui.mainloop()
