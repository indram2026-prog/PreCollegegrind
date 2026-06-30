bpm = int(input("Please input your heart rate: "))
qt_interval = int(input("Please input your QT interval: "))


def classify_ecg(bpm,qt_interval):
    if bpm > 100:
        bpm_class = "Tachycardia"
    elif bpm <= 100 and bpm >= 6:
        bpm_class = "Normal"
    else:
        bpm_class = "Bradycardia"

    
    if qt_interval >= 400:
        qt_class = "Long QT"
    else:
        qt_class = "Normal QT"

    risk = "Low"
    if qt_interval >= 400:
        risk = "High"
    if bpm > 100:
        risk = "High"
    elif bpm < 60:
        risk = "Medium"
    

    return {"Classification": {bpm_class}, "Heart Rate": {bpm}, "QT Interval": {qt_interval}, "QT Class": {qt_class}, "Risk Factor": {risk}}

result = classify_ecg(bpm, qt_interval)
print(result)