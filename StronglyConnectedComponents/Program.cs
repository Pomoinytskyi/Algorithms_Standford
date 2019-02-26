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
			var graph = Graph.ReadFromFile(@".//..//TestData//StronglyConnectedComponents.txt");
			graph.Print("Loaded:");

			System.Console.WriteLine("Reversing");
			graph.Reverse();
			graph.ResetIsVisited(false);

			System.Console.WriteLine("First DFS");
			var result = graph.GetNodeOrdered();
			System.Console.WriteLine($"res - {result.order.Count},  {result.clusters.Count}");

			System.Console.WriteLine("Reverse and reset");
			graph.ResetIsVisited(false);
			graph.Reverse();
			result.order.Reverse();

			System.Console.WriteLine("Second DFS");
			result = graph.GetNodeOrdered(result.order);

			var sizes = result.clusters.Select(kv => kv.Value).OrderBy(v => v);
			var rev = sizes.Reverse();

			foreach (var r in rev.Take(5))
			{
				System.Console.WriteLine(r);
			}
		}
	}
}
