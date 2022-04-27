# shellcheck shell=bash
# no need for shebang - this file is loaded from charts.d.plugin
# SPDX-License-Identifier: GPL-3.0-or-later

# netdata
# real-time performance and health monitoring, done right!
# (C) 2016 Costa Tsaousis <costa@tsaousis.gr>
#

# if this chart is called X.chart.sh, then all functions and global variables
# must start with X_

# _update_every is a special variable - it holds the number of seconds
# between the calls of the _update() function
updates_update_every=600
updates_priority=60000

updates_total_available=0
updates_security_available=0

updates_get() {
	# shellcheck disable=SC2207
	updates_total_available=($(/usr/lib/update-notifier/apt-check 2>&1 | cut -d ';' -f 1))
	if [ $? -ne 0 ]; then return 1; fi
	# shellcheck disable=SC2181
	updates_security_available=($(/usr/lib/update-notifier/apt-check 2>&1 | cut -d ';' -f 2))
	if [ $? -ne 0 ]; then return 1; fi
	return 0
}

# _check is called once, to find out if this chart should be enabled or not
updates_check() {

	# shellcheck disable=2181
	if [ ! -f "/usr/lib/update-notifier/apt-check" ]; then
		# shellcheck disable=SC2154
		error "cannot find executable apt in $PATH"
		return 1
	fi

	# this should return:
	#  - 0 to enable the chart
	#  - 1 to disable the chart

	return 0
}

# _create is called once, to create the charts
updates_create() {
	cat <<EOF
CHART system.updates '' "apt available updates" "updates" updates updates.available line
DIMENSION total '' absolute 1 1
DIMENSION security '' absolute 1 1
EOF

	return 0
}

# _update is called continuously, to collect the values
updates_update() {
	# the first argument to this function is the microseconds since last update
	# pass this parameter to the BEGIN statement (see bellow).

	# do all the work to collect / calculate the values
	# for each dimension
	# remember: KEEP IT SIMPLE AND SHORT

	updates_get || return 1

	# write the result of the work.
	cat <<VALUESEOF
BEGIN system.updates $1
SET total = $((updates_total_available))
SET security = $((updates_security_available))
END
VALUESEOF

	return 0
}
