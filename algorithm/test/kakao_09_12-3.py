def solution(info, query):
    applicants_list = []
    for i in info:
        applicants = i.split(" ")
        applicants_list.append(applicants)

    applicant_list = []
    for j in query:
        j_list = j.split(" ")
        j_list = list(filter(lambda a: a != "and", j_list))
        applicant_list.append(j_list)

    answer = []
    for applicant in applicant_list:
        pass_num = 0
        for num in range(0, len(applicants_list)):
            if applicant[0] != '-':
                if applicant[0] != applicants_list[num][0]:
                    continue
            if applicant[1] != '-':
                if applicant[1] != applicants_list[num][1]:
                    continue
            if applicant[2] != '-':
                if applicant[2] != applicants_list[num][2]:
                    continue
            if applicant[3] != '-':
                if applicant[3] != applicants_list[num][3]:
                    continue
            if int(applicant[4]) > int(applicants_list[num][4]):
                continue
            pass_num += 1
        answer.append(pass_num)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))