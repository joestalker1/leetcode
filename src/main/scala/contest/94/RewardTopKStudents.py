import heapq

class Solution:
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k: int):
        good_feedback = set(positive_feedback)
        bad_feedback = set(negative_feedback)
        min_point = []
        for i in range(len(report)):
            words = report[i].split()
            cur_point = 0
            for word in words:
                if word in bad_feedback:
                    cur_point -= 1
                elif word in good_feedback:
                    cur_point += 3
            min_point.append((cur_point,student_id[i]))
            # if len(min_point) == k:
            #     if min_point[0][0] < cur_point or min_point[0][0] == cur_point and student_id[i] < min_point[0][1]:
            #         heapq.heappop(min_point)
            #         heapq.heappush(min_point,(cur_point,student_id[i]))
            # else:
            #     heapq.heappush(min_point, (cur_point,student_id[i]))
        min_point.sort(key=lambda x:[-x[0],x[1]])
        return [min_point[i][1] for i in range(len(min_point))][:k]

sol = Solution()
print(sol.topStudents(["fkeofjpc","qq","iio"],
["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"],
["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"],
[96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263],3))#[239084671,589204657,43871615]
