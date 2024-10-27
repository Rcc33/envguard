import pandas as pd


def LabDemographic():
    conflict_count = 0
    conflict_event_count = 0
    not_repair = 0
    none = 0
    offline = 0
    app = 0
    event_count = 0
    confilct_type = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    effect_spatial_app = 0
    effect_spatial_env = 0
    effect_time_app = 0
    effect_time_env = 0

    time_related = [0, 0]
    spatial_related = [0, 0]

    for item in range(2, 30):
        file = '../envguard-dataset/data/Lab/output_day_' + str(item) + '.xlsx'
        df = pd.DataFrame(pd.read_excel(file, keep_default_na=False))
        event_count = event_count + (df.shape)[0]
        for index, row in df.iterrows():  # Name Type Location Object TimeStamp PayloadData Source Conflict Fix Method
            if df.iat[index, 7]:
                conflict_event_count = conflict_event_count + 1
                for conflict in (df.iat[index, 7]).split('; '):
                    conflict_count = conflict_count + 1
                    if df.iat[index, 6] == 'app':
                        app = app + 1
                        if 'temperature_up' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[0] = confilct_type[0] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'Brightness.high' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[1] = confilct_type[1] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'Weather' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[2] = confilct_type[2] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'MicrowaveOven' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[3] = confilct_type[3] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'G (TeaRoom.human_undetected & !(TeaRoom.WaterDispenser.on))' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[4] = confilct_type[4] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'humidity_up' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[5] = confilct_type[5] + 1
                            time_related[0] = time_related[0] + 1
                        elif 'AirQuality' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[6] = confilct_type[6] + 1
                            time_related[0] = time_related[0] + 1
                        elif 'Light.off' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[7] = confilct_type[7] + 1
                            time_related[0] = time_related[0] + 1
                        elif 'G((TeaRoom.WaterDispenser.on) ->' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[8] = confilct_type[8] + 1
                            time_related[0] = time_related[0] + 1
                        elif 'Speaker' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[9] = confilct_type[9] + 1
                            time_related[0] = time_related[0] + 1
                    else:
                        if df.iat[index, 6] == 'offline':
                            offline = offline + 1
                        else:
                            none = none + 1
                        if 'temperature_up' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[0] = confilct_type[0] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'Brightness.high' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[1] = confilct_type[1] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'Weather' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[2] = confilct_type[2] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'MicrowaveOven' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[3] = confilct_type[3] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'G (TeaRoom.human_undetected & !(TeaRoom.WaterDispenser.on))' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[4] = confilct_type[4] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'humidity_up' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[5] = confilct_type[5] + 1
                            time_related[1] = time_related[1] + 1
                        elif 'AirQuality' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[6] = confilct_type[6] + 1
                            time_related[1] = time_related[1] + 1
                        elif 'Light.off' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[7] = confilct_type[7] + 1
                            time_related[1] = time_related[1] + 1
                        elif 'G((TeaRoom.WaterDispenser.on) ->' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[8] = confilct_type[8] + 1
                            time_related[1] = time_related[1] + 1
                        elif 'Speaker' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[9] = confilct_type[9] + 1
                            time_related[1] = time_related[1] + 1
                # pattern = re.compile(r'\(\)')
                for fix in (df.iat[index, 8]).split(', '):
                    if fix == '()':
                        not_repair = not_repair + 1

                # match df.iat[index, 6]:
                #     case 'None':
                #         none = none + 1
                #     case 'offline':
                #         offline = offline + 1
                #     case 'app':
                #         app = app + 1

    print(event_count)
    print(conflict_event_count, conflict_count)
    print(confilct_type)
    print(none, app, offline)
    print(spatial_related, time_related)
    print(effect_spatial_app, effect_spatial_env, effect_time_app, effect_time_env)


def HomeDemographic():
    conflict_count = 0
    conflict_event_count = 0
    not_repair = 0
    none = 0
    offline = 0
    app = 0
    event_count = 0
    confilct_type = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    effect_spatial_app = 0
    effect_spatial_env = 0
    effect_time_app = 0
    effect_time_env = 0

    time_related = [0, 0]
    spatial_related = [0, 0]

    for item in range(2, 30):
        file = '../envguard-dataset/data/Home/output_day_' + str(item) + '.xlsx'
        df = pd.DataFrame(pd.read_excel(file, keep_default_na=False))
        event_count = event_count + (df.shape)[0]
        for index, row in df.iterrows():  # Name Type Location Object TimeStamp PayloadData Source Conflict Fix Method
            if df.iat[index, 7]:
                conflict_event_count = conflict_event_count + 1
                for conflict in (df.iat[index, 7]).split('; '):
                    conflict_count = conflict_count + 1
                    if df.iat[index, 6] == 'app':
                        app = app + 1
                        if 'temperature_up' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[0] = confilct_type[0] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'HumanState.detected' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[1] = confilct_type[1] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'Curtain.on' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[2] = confilct_type[2] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'Weather.raining' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[3] = confilct_type[3] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'curtain_on' in conflict:
                            effect_spatial_app = effect_spatial_app + 1
                            confilct_type[4] = confilct_type[4] + 1
                            spatial_related[0] = spatial_related[0] + 1
                        elif 'humidity_up' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[5] = confilct_type[5] + 1
                            time_related[0] = time_related[0] + 1
                        elif 'AirQuality' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[6] = confilct_type[6] + 1
                            time_related[0] = time_related[0] + 1
                        elif 'human_undetected' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[7] = confilct_type[7] + 1
                            time_related[0] = time_related[0] + 1
                        elif 'Fridge' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[8] = confilct_type[8] + 1
                            time_related[0] = time_related[0] + 1
                        elif 'TowelDryer' in conflict:
                            effect_time_app = effect_time_app + 1
                            confilct_type[9] = confilct_type[9] + 1
                            time_related[0] = time_related[0] + 1
                    else:
                        if df.iat[index, 6] == 'offline':
                            offline = offline + 1
                        else:
                            none = none + 1
                        if 'temperature_up' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[0] = confilct_type[0] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'HumanState.detected' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[1] = confilct_type[1] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'Curtain.on' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[2] = confilct_type[2] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'Weather.raining' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[3] = confilct_type[3] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'curtain_on' in conflict:
                            effect_spatial_env = effect_spatial_env + 1
                            confilct_type[4] = confilct_type[4] + 1
                            spatial_related[1] = spatial_related[1] + 1
                        elif 'humidity_up' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[5] = confilct_type[5] + 1
                            time_related[1] = time_related[1] + 1
                        elif 'AirQuality' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[6] = confilct_type[6] + 1
                            time_related[1] = time_related[1] + 1
                        elif 'human_undetected' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[7] = confilct_type[7] + 1
                            time_related[1] = time_related[1] + 1
                        elif 'Fridge' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[8] = confilct_type[8] + 1
                            time_related[1] = time_related[1] + 1
                        elif 'TowelDryer' in conflict:
                            effect_time_env = effect_time_env + 1
                            confilct_type[9] = confilct_type[9] + 1
                            time_related[1] = time_related[1] + 1
                # pattern = re.compile(r'\(\)')
                for fix in (df.iat[index, 8]).split(', '):
                    if fix == '()':
                        not_repair = not_repair + 1

                # match df.iat[index, 6]:
                #     case 'None':
                #         none = none + 1
                #     case 'offline':
                #         offline = offline + 1
                #     case 'app':
                #         app = app + 1

    print(event_count)
    print(conflict_event_count, conflict_count)
    print(confilct_type)
    print(none, app, offline)
    print(spatial_related, time_related)  # 应用/其他
    print(effect_spatial_app, effect_spatial_env, effect_time_app, effect_time_env)


LabDemographic()
# HomeDemographic()
