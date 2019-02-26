using System;
using System.Diagnostics;
using System.Linq;

namespace scc
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("Strongly connected components");

			System.Console.WriteLine("Loading frm file");
			var graph = Graph.ReadFromFile(@".//..//TestData//SccTest.txt");
			graph.Print("Loaded:");

			System.Console.WriteLine("Reversing");
			graph.Reverse();
			graph.ResetIsVited(false);

			System.Console.WriteLine("First DFS");
			var result = graph.GetNodeOrdered();
			System.Console.WriteLine($"res - {result.order.Count},  {result.clusters.Count}");

			System.Console.WriteLine("Reverse and reset");
			graph.ResetIsVited(false);
			result.order.Reverse();

			System.Console.WriteLine("Second DFS");
			result = graph.GetNodeOrdered(result.order);

			var sizes = result.clusters.Select(kv => kv.Value).OrderBy(v => v);
			sizes.Reverse();

			foreach (var r in sizes.Take(3))
			{
				System.Console.WriteLine(r);
			}
		}
	}
}
