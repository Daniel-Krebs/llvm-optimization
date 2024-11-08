import json
from collections import defaultdict


file_path = r"E:\clang 19 json files\ggml_19_3\ggml.dir\llamafile\sgemm.cpp.json"
with open(file_path, 'r') as file:
    trace_data = json.load(file)


trace_events = trace_data.get("traceEvents", [])


function_durations = defaultdict(int)
total_duration = 0
total_percentage=0

for event in trace_events:
    function_name = event.get("name", "Unknown")
    duration = event.get("dur", 0)
    function_durations[function_name] += duration
    total_duration+=duration


# Sort the results by total duration in descending order
sorted_function_durations = sorted(function_durations.items(), key=lambda x: x[1], reverse=True)

# Display the total duration for each unique function
print("Total duration for each unique function:")
for function, function_duration in sorted_function_durations:
    percentage = (function_duration / total_duration) * 100 if total_duration else 0
    total_percentage+=percentage
    #print(f"{percentage}")

print(total_duration)