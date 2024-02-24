from compliance_calculator import start_process
# from build.lib.compliance_calculator import start_process

if __name__ == '__main__':
    k = start_process('../loadingcurve.csv','../unloadingcurve.csv')
    print(k)
