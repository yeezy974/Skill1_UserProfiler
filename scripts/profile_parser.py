# 伪代码：意图识别逻辑
def check_user_intent(user_input):
    keywords = ["投递", "简历", "找工作", "匹配", "官网", "招聘"]
    if any(k in user_input for k in keywords):
        return "TRIGGER_SKILL_01"
    return "IDLE"