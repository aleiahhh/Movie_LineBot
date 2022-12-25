from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=['user', 'menu', 'now_playing', 'popular', 'top_rated', 'upcoming', 'overview', 'fsm'],
        transitions=[
            {
                "trigger":"advance",
                "source":"user",
                "dest":"menu",
                "conditions":"is_going_to_menu",
            },
            {
                "trigger":"advance",
                "source":"menu",
                "dest":"now_playing",
                "conditions":"is_going_to_now_playing",
            },
            {
                "trigger":"advance",
                "source":"menu",
                "dest":"popular",
                "conditions":"is_going_to_popular",
            },
            {
                "trigger":"advance",
                "source":"menu",
                "dest":"top_rated",
                "conditions":"is_going_to_top_rated",
            },
            {
                "trigger":"advance",
                "source":"menu",
                "dest":"upcoming",
                "conditions":"is_going_to_upcoming",
            },
            {
                "trigger":"advance",
                "source":"menu",
                "dest":"fsm",
                "conditions":"is_going_to_fsm",
            },
            {
                "trigger":"advance",
                "source":"now_playing",
                "dest":"menu",
                "conditions":"is_going_to_menu",
            },
            {
                "trigger":"advance",
                "source":"now_playing",
                "dest":"overview",
                "conditions":"is_going_to_overview",
            },
            {
                "trigger":"advance",
                "source":"popular",
                "dest":"menu",
                "conditions":"is_going_to_menu",
            },
            {
                "trigger":"advance",
                "source":"popular",
                "dest":"overview",
                "conditions":"is_going_to_overview",
            },
            {
                "trigger":"advance",
                "source":"top_rated",
                "dest":"menu",
                "conditions":"is_going_to_menu",
            },
            {
                "trigger":"advance",
                "source":"top_rated",
                "dest":"overview",
                "conditions":"is_going_to_overview",
            },
            {
                "trigger":"advance",
                "source":"upcoming",
                "dest":"menu",
                "conditions":"is_going_to_menu",
            },
            {
                "trigger":"advance",
                "source":"upcoming",
                "dest":"overview",
                "conditions":"is_going_to_overview",
            },
            {
                "trigger":"advance",
                "source":"fsm",
                "dest":"menu",
                "conditions":"is_going_to_menu",
            },
            {
                "trigger":"advance",
                "source":"overview",
                "dest":"menu",
                "conditions":"is_going_to_menu",
            },
            {
                "trigger":"go_back",
                "source":"overview",
                "dest":"user",
            },
        ],
        initial = "user",
        auto_transitions = False,
        show_conditions = True,
    )

    return machine

    