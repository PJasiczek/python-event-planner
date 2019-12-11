import event
import datetime
import calendar

ans=True
eventList=[]

while ans:
    print ("\n\t\033[1;34;40mDzisiejszy czas "
    , datetime.datetime.today(), "\033[0m",
    """\n
    1.Dodaj wydarzenie
    2.Przeglądaj kalendarz
    3.Usuń wydarzenie
    4.Przeglądaj najbliższe zapisane wydarzenia
    5.Wyjście
    """)
    ans=input("Wybierz opcje: ")
    if ans=="1":
      print("\n\tDodaj wydarzenie\n")

      ev_name = input("Nazwa wydarzenia: ")
      ev_year = input("Rok: ")
      ev_mouth = input("Miesiąc: ")
      ev_day = input("Dzień: ")
      ev_hour = input("Godzina rozpoczęcia: ")
      ev_minute = input("Minuta rozpoczęcia: ")

      ev = event.Event(ev_name, int(ev_year), int(ev_mouth), int(ev_day), int(ev_hour), int(ev_minute))

      now = datetime.datetime.now()
      ev_now = event.Event("", int(now.year), int(now.month), int(now.day), int(now.hour), int(now.minute))

      for x in range(len(eventList)):
        if(eventList[x] == ev):
            print("\n\033[1;31;40m Wydarzenie już istnieje\033[0m")
        elif(ev_now < ev):
            eventList.append(ev)  # add event to list with events

      if((not eventList) and (ev_now < ev)):
            eventList.append(ev)  # add event to list with events
      elif(ev_now > ev):
          print("\n\033[1;31;40m Nieprawidłowa data wydarzenia\033[0m")

    elif ans=="2":
      print("\n\tPrzeglądaj kalendarz\n")

      ev_year = input("Rok: ")
      ev_mouth = input("Miesiąc: ")

      cal = calendar.month(int(ev_year), int(ev_mouth))

      print(cal)
    elif ans=="3":
      print("\n\tUsuń wydarzenie\n")

      for x in range(len(eventList)):
          if x is not None:
            eventList[x].displayEvent()

      index = input("\nUsuń wydarzenie z podanej listy o indeksie: ")

      try :
        eventList.pop(int(index)-1)
        print("\033[1;32;40mUsunięto!\033[0m")
      except IndexError:
        print("\n\033[1;31;40mIndeks poza rozmiarem listy\033[0m")

    elif ans=="4":
      print("\n\tPrzeglądaj najbliższe zapisane wydarzenia:\n")

      for x in range(len(eventList)):
          if x is not None:
            eventList[x].displayEvent()
    elif ans == "5":
      print("\n\tWyjście\n")
      exit()
    elif ans !="":
      print("\n\tSpróbuj ponownie!")

