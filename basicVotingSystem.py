nominee1=input("Enter the name of 1st nominee : ")
nominee2=input("Enter the name of 2nd nominee : ")

nominee1_votes=0
nominee2_votes=0

voter_id=[1,2,3,4,5,6,7,8,9,10]

no_of_voter=len(voter_id)

while True:

    if voter_id==[]:
        print("Voting session is over")
        if nominee1_votes>nominee2_votes:
            percent=(nominee1_votes/no_of_voter)*100
            print(nominee1,"has won the election with ",percent,"%")
            break
        elif nominee2_votes>nominee1_votes:
            percent=(nominee2_votes/no_of_voter)*100
            print(nominee2,"has won the election with ",percent,"%")
            break
        else:
            print("Both have equal number of votes")
            break
        
    voter=int(input("Enter your voter id : "))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter)
        print("-----------------------------------")
        print("To give vote to ",nominee1,"Press 1")
        print("To give vote to ",nominee2,"Press 2")
        print("-----------------------------------")
        
        vote=int(input("Enter your choice : "))
        if vote==1:
            nominee1_votes+=1
            print(nominee1,"Thanks you for your support")
        elif vote==2:
            nominee2_votes+=1
            print(nominee2,"Thanks you for your support")
        else:
            print("Wrong choice ")
