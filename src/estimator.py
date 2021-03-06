def estimator(data):
     reportedCases= int(input())
     timeToElapse= int(input())
     totalHospitalBeds = int(input())
     avgDailyIncomeInUSD = float(input())
     population = int(input())
     return reportedCases,timeToElapse,totalHospitalBeds,avgDailyIncomeInUSD,population
def Impact():
    reportedCases,timeToElapse,totalHospitalBeds,avgDailyIncomeInUSD,population = estimator("data")
    currentlyInfected = reportedCases*10
    infectionsByRequestedTime = currentlyInfected*(2**(timeToElapse//3))
    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    hospitalBedsByRequestedTime = int((0.35*totalHospitalBeds)-severeCasesByRequestedTime)
    casesForICUByRequestedTime = int(0.05* infectionsByRequestedTime)
    casesForVentilatorsByRequestedTime = int(0.02*infectionsByRequestedTime)
    dollarsInFlight= int((0.65*1.5*infectionsByRequestedTime)/timeToElapse)
    return currentlyInfected,infectionsByRequestedTime,severeCasesByRequestedTime, hospitalBedsByRequestedTime, casesForICUByRequestedTime,casesForVentilatorsByRequestedTime,dollarsInFlight
def severeImpact():
    reportedCases,timeToElapse,totalHospitalBeds, avgDailyIncomeInUSD = estimator("data")
    currentlyInfected = reportedCases*50
    infectionsByRequestedTime = currentlyInfected*(2**(timeToElapse//3))
    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    hospitalBedsByRequestedTime = int((0.35*totalHospitalBeds)-severeCasesByRequestedTime)
    casesForICUByRequestedTime = int(0.05* infectionsByRequestedTime)
    casesForVentilatorsByRequestedTime = int(0.02*infectionsByRequestedTime)
    dollarsInFlight= int((0.65*1.5*infectionsByRequestedTime)/timeToElapse)
    return currentlyInfected,infectionsByRequestedTime,severeCasesByRequestedTime, hospitalBedsByRequestedTime, casesForICUByRequestedTime,casesForVentilatorsByRequestedTime,dollarsInFlight
def estimate():
     return estimator("data"), Impact(),severeImpact()
