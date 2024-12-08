def get_between(lines, a, b):
    l = []
    start = False
    for line in lines:
        if line == a:
            start = True
        elif start and line == b:
            return l
        elif start:
            l.append(line)
    return l

def get_value(map_lines, seed):
    for line in map_lines:
        destination_start, source_start, length = [int(x) for x in line.split()]
        if source_start <= seed <= source_start + length - 1:
            shift = seed - source_start
            destination = destination_start + shift
            return destination
    return seed

def flatten(xss):
    return [x for xs in xss for x in xs]

def get_range_seeds(seeds):
    seeds = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    return seeds

with open('5/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    seeds = [int(seed) for seed in lines[0].split(':')[-1].split()]
    seeds = get_range_seeds(seeds)

    seed_soil = get_between(lines, 'seed-to-soil map:', '')
    soil_fertilizer = get_between(lines, 'soil-to-fertilizer map:', '')
    fertilizer_water = get_between(lines, 'fertilizer-to-water map:', '')
    water_light = get_between(lines, 'water-to-light map:', '')
    light_temperature = get_between(lines, 'light-to-temperature map:', '')
    temperature_humidity = get_between(lines, 'temperature-to-humidity map:', '')
    humidity_location = get_between(lines, 'humidity-to-location map:', '')

    locations = []
    for seed_range in seeds:
        print(seed_range)
        for seed in seed_range:
            soil = get_value(seed_soil, seed)
            fertilizer = get_value(soil_fertilizer, soil)
            water = get_value(fertilizer_water, fertilizer)
            light = get_value(water_light, water)
            temperature = get_value(light_temperature, light)
            humidity = get_value(temperature_humidity, temperature)
            location = get_value(humidity_location, humidity)
            locations.append(location)

    print(min(locations))