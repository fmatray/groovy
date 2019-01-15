def get_status_color(status):
    colors = {
        'Draft': 'badge-info',
        'On going': 'badge-success',
        'Released': 'badge-success',
        'Retired': 'badge-danger',
        'Abort': 'badge-danger'
    }
    return colors[status]
