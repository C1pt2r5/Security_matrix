from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Sample data embedded in the script
data = [
    {"incident_id": 1, "type": "Phishing", "severity": "High", "department": "Finance", "time_to_resolve_hours": 10},
    {"incident_id": 2, "type": "Malware", "severity": "Medium", "department": "IT", "time_to_resolve_hours": 5},
    {"incident_id": 3, "type": "Data Breach", "severity": "Critical", "department": "HR", "time_to_resolve_hours": 30},
    {"incident_id": 4, "type": "Phishing", "severity": "Medium", "department": "Finance", "time_to_resolve_hours": 8},
    {"incident_id": 5, "type": "Malware", "severity": "Low", "department": "IT", "time_to_resolve_hours": 3},
    {"incident_id": 6, "type": "Phishing", "severity": "High", "department": "Marketing", "time_to_resolve_hours": 12},
    {"incident_id": 7, "type": "Data Breach", "severity": "Critical", "department": "IT", "time_to_resolve_hours": 25},
]

# Function to calculate metrics
def calculate_metrics(data):
    incidents_by_type = {}
    severity_distribution = {}
    incidents_by_department = {}
    total_time_to_resolve = 0
    total_incidents = len(data)
    
    for incident in data:
        # Count incidents by type
        incident_type = incident['type']
        if incident_type in incidents_by_type:
            incidents_by_type[incident_type] += 1
        else:
            incidents_by_type[incident_type] = 1
        
        # Count incidents by severity
        severity = incident['severity']
        if severity in severity_distribution:
            severity_distribution[severity] += 1
        else:
            severity_distribution[severity] = 1
        
        # Count incidents by department
        department = incident['department']
        if department in incidents_by_department:
            incidents_by_department[department] += 1
        else:
            incidents_by_department[department] = 1
        
        # Sum time to resolve
        total_time_to_resolve += incident['time_to_resolve_hours']
    
    # Calculate average time to resolve
    avg_time_to_resolve = total_time_to_resolve / total_incidents if total_incidents > 0 else 0

    return {
        "incidents_by_type": incidents_by_type,
        "severity_distribution": severity_distribution,
        "avg_time_to_resolve": avg_time_to_resolve,
        "incidents_by_department": incidents_by_department
    }

# Function to display metrics attractively
def display_metrics(metrics):
    print(Fore.CYAN + Style.BRIGHT + "\nSecurity Metrics Summary")
    print(Fore.CYAN + Style.BRIGHT + "=" * 24)
    print(f"{Fore.YELLOW}Average Time to Resolve Incidents: {Fore.GREEN}{metrics['avg_time_to_resolve']:.2f} hours")
    
    print(Fore.CYAN + Style.BRIGHT + "\nNumber of Incidents by Type:")
    print(Fore.CYAN + Style.BRIGHT + "-" * 28)
    for type_, count in metrics['incidents_by_type'].items():
        print(f"{Fore.YELLOW}  {type_}: {Fore.GREEN}{count}")
    
    print(Fore.CYAN + Style.BRIGHT + "\nIncident Severity Distribution:")
    print(Fore.CYAN + Style.BRIGHT + "-" * 30)
    for severity, count in metrics['severity_distribution'].items():
        print(f"{Fore.YELLOW}  {severity}: {Fore.GREEN}{count}")
    
    print(Fore.CYAN + Style.BRIGHT + "\nIncidents Per Department:")
    print(Fore.CYAN + Style.BRIGHT + "-" * 26)
    for department, count in metrics['incidents_by_department'].items():
        print(f"{Fore.YELLOW}  {department}: {Fore.GREEN}{count}")

# Main function to run the tool
def main():
    metrics = calculate_metrics(data)
    display_metrics(metrics)

# Run the script
if _name_ == "_main_":
    main()
