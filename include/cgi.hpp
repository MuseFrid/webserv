#pragma once

# include "Webserv.hpp"
# include <cstdio>
# include <cstdlib>
#include <sys/wait.h>

class tempThrow : public std::exception
{
	public:
		const char*	what(void) const throw()
		{
			return ("TEMP THROW -- TO DELETE LATER");
		}
}; // TEMP THROW -- TO DELETE LATER 